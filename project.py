import streamlit as st
import speech_recognition as sr
import requests
from pypdf import PdfReader
from docx import Document
from PIL import Image
import pytesseract
import cv2
import os
import numpy as np
import easyocr
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- OLLAMA API URL ---
url = "http://localhost:11434/api/chat"

@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

ocr_reader = load_ocr()

from callbacks import(
    init_session_state,
    handle_new_chat_click,
    toggle_upload,
    toggle_mic,
    handle_query_submit,
    load_chat,
    handle_upload_change,
)
from styles import inject_css

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="project.py",
    layout="centered"
)

# --- INITIALIZE SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
if "upload_clicked" not in st.session_state:
    st.session_state.upload_clicked = False
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "mic_active" not in st.session_state:
    st.session_state.mic_active = False
if "input_key" not in st.session_state:
    st.session_state.input_key = 0
if "recent_chats" not in st.session_state:
    st.session_state.recent_chats = []


# --- VOICE INPUT FUNCTION ---
def capture_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak now!")
        audio_data = recognizer.listen(source, phrase_time_limit=5)
        st.info("⏳ Processing your voice...")

    try:
        text = recognizer.recognize_google(audio_data)
        st.success(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        st.warning("❌ Sorry, I couldn’t understand your speech.")
        return ""
    except sr.RequestError as e:
        st.error(f"⚠️ Could not request results; {e}")
        return ""


# --- FILE TEXT EXTRACTION ---
def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.type
    extracted_text = ""
    try:
       # 🖼️ Handle images
       if file_type.startswith("image/"):
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        extracted_text = "".join(ocr_reader.readtext(image_np, detail=0))
      
       elif file_type == "application/pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
         extracted_text += page.extract_text() or ""
         
       elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                extracted_text += para.text + "\n"

       elif file_type == "text/plain":
            extracted_text = uploaded_file.read().decode("utf-8")

       else:
            st.warning("Unsupported file type. Please upload image, PDF, or text document.")
            return ""

       return extracted_text.strip()
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        return ""

# --- SIDEBAR ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-container">', unsafe_allow_html=True)

        st.button(
            "➕ New Chat",
            on_click=handle_new_chat_click,
            key="new_chat_button",
            use_container_width=True
        )

        st.markdown("<h3>💬 Recent chats</h3>", unsafe_allow_html=True)

        for i, chat in enumerate(st.session_state.recent_chats):
            st.button(
                chat["title"],
                on_click=load_chat,
                args=(i,),
                key=f"chat_load_btn_{i}",
                use_container_width=True
            )

        st.markdown(
            """
            <div class="profile">
                <div class="avatar">KA</div>
                <div class="details">
                    <div class="name">Karri Manoj</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- HEADER ---
def render_header():
   if not st.session_state.get("chat_started", False):
    st.markdown("""
     <style>
      [data-testid="stHeader"]::after
     {
      content: " CodeGenie  ";
      font-size: 19px;
      color: #ff4b4b;
      display: flex;
      align-items: center;
       gap: 8px;
    }
 </style>
""", unsafe_allow_html=True)
    
# --- CHAT HISTORY ---
def render_chat_history():
    chat_history_class = "chat-history-container"
    if st.session_state.chat_started:
        chat_history_class += " visible"

    st.markdown(f'<div class="{chat_history_class}">', unsafe_allow_html=True)

    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]

        row_class = "chat-message-row " + (
            "user-message-row" if role == "user" else "ai-message-row"
        )
        bubble_class = "chat-message-bubble " + (
            "user-message-bubble" if role == "user" else "ai-message-bubble"
        )

        st.markdown(
            f"""
            <div class="{row_class}">
                <div class="{bubble_class}">
                    {content}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


# --- INPUT AREA (Text + Mic) ---
def render_input_area():
    search_bar_class = "search-bar-container"
    if st.session_state.chat_started:
        search_bar_class += " fixed-bottom"
    st.markdown(f'<div class="{search_bar_class}">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.4, 3.8, 0.4])
    current_input_key = f"query_input_value_{st.session_state.input_key}"

    with col1:
        st.button(
            "➕",
            on_click=toggle_upload,
            key=f"plus_button_{st.session_state.input_key}",
            help="Click to upload a file"
        )

    with col2:
        user_input = st.text_area(
            label="chat_input",
            placeholder="Ask anything....",
            height=2,
            key=current_input_key
        )

    with col3:
        mic_icon = "🎙️" if st.session_state.get("mic_active", False) else "🎤"
        st.button(
            mic_icon,
            on_click=toggle_mic,
            key=f"mic_button_{st.session_state.get('input_key', 0)}",
            help="Click to toggle voice input"
        )

    if st.session_state.get("mic_active", False):
        voice_text = capture_voice_input()
        if voice_text: 
            user_input = voice_text
            st.session_state.mic_active = False

    st.markdown('</div>', unsafe_allow_html=True)

    if user_input:
        st.session_state.chat_started = True
        st.session_state.messages.append({"role": "user", "content": user_input})

        payload = {
            "model": "llama3.2",
            "messages": st.session_state.messages,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload).json()
            assistant_msg = response["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
        except Exception as e:
            st.error(f" Error contacting Ollama: {e}")


# --- FILE UPLOADER ---
def render_file_uploader():
    if st.session_state.upload_clicked and st.session_state.uploaded_file is None:
        st.markdown('<div class="file-uploader-fixed">', unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Upload your file here",
            key="file_uploader_main",
            type=["pdf", "png", "jpg", "jpeg", "txt", "docx"],
            label_visibility="collapsed"
        )

        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
            st.toast(f"Uploaded: {uploaded_file.name}")

            extracted_text = extract_text_from_file(uploaded_file)

            if extracted_text:
                st.session_state.chat_started = True
                st.session_state["ocr_text"] = extracted_text
 
                preview_text = extracted_text[:500] 

                st.session_state.messages.append({
                  "role": "user",
                   "content": f"📎 Extracted Text from {uploaded_file.name}:\n\n{preview_text}"
                })
                if "ocr_text" in st.session_state:
                  with st.expander(" Show Full Extracted Text"):
                   st.text_area("Extracted text", st.session_state["ocr_text"], height=300)
                payload = {
                    "model": "llama3.2",
                    "messages": st.session_state.messages,
                    "stream": False
                }

                try:
                    response = requests.post(url, json=payload).json()
                    assistant_msg = response["message"]["content"]
                    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
                except Exception as e:
                    st.error(f"Error contacting Ollama: {e}")

        st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN ---
def main():
    init_session_state()
    inject_css()
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">',
        unsafe_allow_html=True
    )
    render_header()
    render_sidebar()
   
    st.markdown('<div class="main-content">', unsafe_allow_html=True) 
    title_class = "title"
    if st.session_state.chat_started:
        title_class += " hidden"
    st.markdown(f'<h1 class="{title_class}">What\'s on your mind today?</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    render_chat_history()
    render_file_uploader()
    render_input_area()
   
    
    if st.session_state.uploaded_file is not None:
        st.toast(f"File uploaded successfully: {st.session_state.uploaded_file.name}")

if __name__ == "__main__":
    main()
