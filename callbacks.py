import streamlit as st
import time

# --- SESSION STATE INITIALIZATION ---

def init_session_state():
    """Initializes all necessary session state variables."""
    if "upload_clicked" not in st.session_state:
        st.session_state.upload_clicked = False
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None
    if "mic_active" not in st.session_state:
        st.session_state.mic_active = False
    if "recent_chats" not in st.session_state:
        st.session_state.recent_chats = [
            {"title": "Summarise the code...", "messages": []},
            {"title": "Generate Python code to print name...", "messages": []},
        ]
    if "new_chat_clicked" not in st.session_state:
        st.session_state.new_chat_clicked = False
    if "chat_started" not in st.session_state:
        st.session_state.chat_started = False
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "input_key" not in st.session_state:
        st.session_state.input_key = 0
    if "query_input_value" not in st.session_state:
        st.session_state.query_input_value = ""

# --- HELPER FUNCTIONS (CALLBACKS) ---
def toggle_upload():
    """Toggles the visibility of the file uploader."""
    st.session_state.upload_clicked = not st.session_state.upload_clicked
    if not st.session_state.upload_clicked:
        st.session_state.uploaded_file = None
        st.session_state.input_key += 1 

def handle_upload_change():
    """Handles the file upload event and hides the uploader."""
    uploaded_file = st.session_state.file_uploader_main
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
        st.session_state.upload_clicked = False 
        st.session_state.input_key += 1 

def load_chat(chat_index):
    """Loads a chat from recent_chats into the main window."""
    if 0 <= chat_index < len(st.session_state.recent_chats):
        if st.session_state.chat_started and st.session_state.messages:
            _save_current_chat()

        chat_to_load = st.session_state.recent_chats[chat_index]
        st.session_state.messages = chat_to_load["messages"].copy()
        st.session_state.chat_started = True
        st.session_state.query_input_value = ""
        st.session_state.input_key += 1
        # st.rerun() REMOVED: The next natural rerun is sufficient.

def _save_current_chat():
    """Internal function to save the current chat to recent_chats."""
    if not st.session_state.messages:
        return

    first_user_message = next((msg["content"] for msg in st.session_state.messages if msg["role"] == "user"), "New Chat")
    
    title = first_user_message[:30].strip()
    if len(first_user_message) > 30:
        title += "..."

    new_chat_entry = {
        "title": title,
        "messages": st.session_state.messages.copy()
    }
    
    if new_chat_entry["title"] != "New Chat":
        if not any(entry["title"] == title for entry in st.session_state.recent_chats):
             st.session_state.recent_chats.insert(0, new_chat_entry)
        
        st.session_state.recent_chats = st.session_state.recent_chats[:10]


def reset_chat_session():
    """Resets the current chat session to the initial state."""
    _save_current_chat()
    
    st.session_state.chat_started = False
    st.session_state.messages = []
    st.session_state.query_input_value = ""
    st.session_state.input_key += 1
    # st.rerun() REMOVED: The next natural rerun is sufficient.

def handle_new_chat_click():
    """Saves the current chat and resets the session for a new chat."""
    reset_chat_session()

def toggle_mic():
    """Toggles the microphone active state (simulated)."""
    st.session_state.mic_active = not st.session_state.mic_active
    if st.session_state.mic_active:
        st.toast("Microphone ON")
    else:
        st.toast("Microphone OFF")

def handle_query_submit():
    """Handles the submission of the user's query from the text input."""
    # We retrieve the value from the current key in session state
    user_query = st.session_state.get(f"query_input_value_{st.session_state.input_key}", "")
    
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.session_state.chat_started = True
        
        # We must increment the key *after* setting the message but *before* the subsequent code
        # runs, to ensure the input field is clear on the next script execution.
        st.session_state.input_key += 1 
        
        simulate_ai_response(user_query)
        # Note: The script is automatically rerun after this function returns due to the
        # st.text_input on_change event.

def simulate_ai_response(user_query):
    """Simulates a response from the AI model."""
    
    file_context = ""
    if st.session_state.uploaded_file:
        file_context = f" (Context from file: {st.session_state.uploaded_file.name})"
        st.session_state.uploaded_file = None 

    response_text = f"Hello! I received your query: **'{user_query}'**{file_context}. I am now processing your request for code generation and correction."
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    # st.rerun() REMOVED: No need to call st.rerun() here as the preceding callback
    # already triggered the script rerun.
