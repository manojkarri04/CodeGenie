import streamlit as st
import easyocr
import speech_recognition as sr
import requests
import json
import numpy as np
from PIL import Image
from pypdf import PdfReader
from docx import Document
from typing import List, Dict, Optional, Any, Union

# Local Imports
# Ensure these files exist in your directory as per your original setup
from callbacks import (
    handle_new_chat_click,
    toggle_upload,
    toggle_mic,
    load_chat
)
from styles import inject_css

# --- CONFIGURATION ---
class AppConfig:
    PAGE_TITLE = "Code Genie"
    PAGE_ICON = "Logo-removebg-preview.png"
    LOGO_IMAGE = "Logo1-removebg-preview.png"
    GITHUB_LINK = "https://github.com/manojkarri04/CodeGenie"
    OLLAMA_URL = "http://localhost:11434/api/chat"
    MODEL_NAME = "CodeGenie"
    MAX_IMG_WIDTH = 1000
    VOICE_TIMEOUT = 5
    VOICE_PHRASE_LIMIT = 10

# --- INITIALIZATION ---
def configure_page():
    """Sets up basic page config and logo."""
    st.set_page_config(
        page_title=AppConfig.PAGE_TITLE,
        page_icon=AppConfig.PAGE_ICON,
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # Graceful fallback for st.logo (Streamlit 1.35+)
    if hasattr(st, "logo"):
        st.logo(
            AppConfig.LOGO_IMAGE, 
            link=AppConfig.GITHUB_LINK, 
            icon_image=AppConfig.PAGE_ICON
        )

def init_session_state():
    """Initializes all session state variables."""
    defaults = {
        "messages": [],
        "chat_started": False,
        "upload_clicked": False,
        "uploaded_file": None,
        "mic_active": False,
        "input_key": 0,
        "recent_chats": [],
        "listening": False,
        "audio": None
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

# --- SERVICES: OCR ---
@st.cache_resource
def load_ocr_reader():
    return easyocr.Reader(['en'], gpu=False)

@st.cache_data(show_spinner=True)
def process_file_ocr(file_bytes: Any, file_type: str) -> str:
    """Handles text extraction from Images, PDFs, DOCX, and Text files."""
    try:
        if file_type.startswith("image/"):
            reader = load_ocr_reader()
            image = Image.open(file_bytes).convert("L")
            
            # Resize if too large for performance
            if image.width > AppConfig.MAX_IMG_WIDTH:
                ratio = AppConfig.MAX_IMG_WIDTH / image.width
                image = image.resize((AppConfig.MAX_IMG_WIDTH, int(image.height * ratio)))
            
            image_np = np.array(image)
            return " ".join(reader.readtext(image_np, detail=0, paragraph=True))
        
        elif file_type == "application/pdf":
            reader = PdfReader(file_bytes)
            return "".join(page.extract_text() or "" for page in reader.pages)
        
        elif "wordprocessingml" in file_type:
            doc = Document(file_bytes)
            return "\n".join(p.text for p in doc.paragraphs)
        
        elif file_type == "text/plain":
            return file_bytes.read().decode("utf-8")
            
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return ""
    
    return ""

# --- SERVICES: VOICE ---
def process_voice_input() -> str:
    """Captures and processes audio input using SpeechRecognition."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        if st.session_state.listening:
            st.info("🎙️ Listening... Speak now!")
            try:
                audio_data = recognizer.listen(
                    source, 
                    timeout=AppConfig.VOICE_TIMEOUT, 
                    phrase_time_limit=AppConfig.VOICE_PHRASE_LIMIT
                )
                st.session_state.audio = audio_data
            except sr.WaitTimeoutError:
                st.warning("❌ No speech detected.")
                return ""
        else:
            # Process captured audio
            if st.session_state.get("audio"):
                st.info("⏳ Processing your voice...")
                audio_data = st.session_state.audio
                st.session_state.audio = None  # Reset buffer

                try:
                    text = recognizer.recognize_google(audio_data)
                    st.success(f"✅ You said: {text}")
                    return text
                except sr.UnknownValueError:
                    st.warning("❌ Sorry, I couldn't understand your speech.")
                except sr.RequestError as e:
                    st.error(f"⚠️ Service error: {e}")
    return ""

# --- SERVICES: API ---
def stream_ollama_response(messages: List[Dict[str, str]]) -> str:
    """Streams response from the Ollama API and updates the UI in real-time."""
    payload = {
        "model": AppConfig.MODEL_NAME, 
        "messages": messages, 
        "stream": True
    }
    placeholder = st.empty()
    full_text = ""
    
    try:
        with requests.post(AppConfig.OLLAMA_URL, json=payload, stream=True) as response:
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        body = json.loads(line)
                        if "message" in body and "content" in body["message"]:
                            full_text += body["message"]["content"]
                            _render_streaming_bubble(placeholder, full_text)
                        
                        if body.get("done", False):
                            break
            else:
                full_text = "Error: Could not connect to CodeGenie."
    except Exception as e:
        full_text = f"Error: {str(e)}"

    # Final render without cursor
    placeholder.html(f"""
        <div class="chat-message-row ai-message-row">
            <div class="chat-message-bubble ai-message-bubble">{full_text}</div>
        </div>
    """)
    return full_text

def _render_streaming_bubble(placeholder, text: str):
    """Helper to render the intermediate streaming bubble."""
    placeholder.markdown(f"""
        <div class="chat-message-row ai-message-row">
            <div class="chat-message-bubble ai-message-bubble">{text}▌</div>
        </div>
    """, unsafe_allow_html=True)

# --- UI COMPONENTS ---
def render_sidebar():
    """Renders the sidebar with chat history and profile."""
    with st.sidebar:
        st.button("➕ New Chat", on_click=handle_new_chat_click, use_container_width=True)
        st.divider()
        st.markdown("<h3>💬 Recent chats</h3>", unsafe_allow_html=True)
        
        if "recent_chats" in st.session_state:
            for i, chat in enumerate(st.session_state.recent_chats):
                st.button(
                    chat["title"], 
                    on_click=load_chat, 
                    args=(i,), 
                    key=f"chat_{i}", 
                    use_container_width=True
                )
        
        st.html(f"""
            <div class="profile" style="display: flex; align_items: center; gap: 10px; margin-top: 10px;">
                  <div class="avatar" style="background: #eee; padding: 8px; border-radius: 50%; font-weight: bold;">CG</div>
                  <div class="details"><div class="name" style="font-weight: bold;">Code Genie</div></div>
            </div>          
        """)

def render_chat_history():
    """Renders existing messages in the session."""
    container_cls = "chat-history-container visible" if st.session_state.chat_started else "chat-history-container"
    st.markdown(f'<div class="{container_cls}">', unsafe_allow_html=True)
    
    # Display last 40 messages
    for msg in st.session_state.messages[-40:]:
        role = msg["role"]
        row_cls = "user-message-row" if role == "user" else "ai-message-row"
        bubble_cls = "user-message-bubble" if role == "user" else "ai-message-bubble"
        
        st.markdown(f"""
        <div class="chat-message-row {row_cls}">
            <div class="chat-message-bubble {bubble_cls}">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Spacer
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_file_uploader():
    """Handles the file upload logic overlay."""
    if st.session_state.upload_clicked and st.session_state.uploaded_file is None:
        st.session_state.chat_started = True
        st.markdown(
            '<div class="fixed-footer" style="bottom: 80px; background: transparent; border: none;">', 
            unsafe_allow_html=True
        )
        
        uploaded = st.file_uploader("Upload your file", type=["pdf", "png", "jpg", "jpeg", "txt", "docx"])
        
        if uploaded:
            st.session_state.uploaded_file = uploaded
            text = process_file_ocr(uploaded, uploaded.type)
            if text:
                preview = text[:500]
                _handle_user_submission(f"📎 Extracted text:\n\n{preview}")
            
            st.session_state.upload_clicked = False
            st.rerun()
            
        st.markdown("</div>", unsafe_allow_html=True)

def render_input_area():
    """Renders the bottom input bar and handles text/voice interactions."""
    footer_cls = "fixed-footer" if st.session_state.chat_started else "search-bar-container"

    st.markdown(f'<div class="{footer_cls}">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 10, 1])
    
    with col1:
        st.button("➕", on_click=toggle_upload, key="btn_upload")
    
    with col2:
        user_input = st.text_area(
            "Message CodeGenie...", 
            height=52, 
            key=f"query_{st.session_state.input_key}",
            label_visibility="collapsed",
            placeholder="Message CodeGenie..."
        )
    
    with col3:
        mic_icon = "🎙️" if st.session_state.get("mic_active", False) else "🎤"
        st.button(mic_icon, on_click=toggle_mic, key="btn_mic")
    
    # Handle Voice Logic
    if st.session_state.get("mic_active", False):
        st.session_state.listening = not st.session_state.listening
        voice_text = process_voice_input()
        if voice_text:
            user_input = voice_text
            st.session_state.mic_active = False # Turn off mic after success

    st.markdown("</div>", unsafe_allow_html=True)

    # Submission Trigger
    if user_input and user_input.strip():
        _handle_user_submission(user_input)

def _handle_user_submission(content: str):
    """Common logic to append message, stream response, and update state."""
    st.session_state.chat_started = True
    st.session_state.messages.append({"role": "user", "content": content})
    
    # Get AI Response
    full_text = stream_ollama_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": full_text})
    
    # Reset input
    st.session_state.input_key += 1
    st.rerun()

# --- MAIN EXECUTION ---
def main():
    configure_page()
    init_session_state()
    inject_css()

    if not st.session_state.chat_started:
        st.markdown('<h1 class="title">What can I help with?</h1>', unsafe_allow_html=True)

    render_chat_history()
    render_file_uploader()
    render_input_area()
    render_sidebar()

if __name__ == "__main__":
    main()