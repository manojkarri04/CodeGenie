import streamlit as st

def handle_new_chat_click():
    if st.session_state.messages:
        title = st.session_state.messages[0]["content"][:30] + "..."
        st.session_state.recent_chats.insert(
            0, {"title": title, "messages": st.session_state.messages.copy()}
        )
        st.session_state.recent_chats = st.session_state.recent_chats[:10]

    st.session_state.messages = []
    st.session_state.chat_started = False
    st.session_state.input_key += 1

def toggle_upload():
    st.session_state.upload_clicked = not st.session_state.upload_clicked
    if not st.session_state.upload_clicked:
        st.session_state.uploaded_file = None

def toggle_mic():
    st.session_state.mic_active = not st.session_state.mic_active
    st.toast("Microphone ON" if st.session_state.mic_active else "Microphone OFF")

def load_chat(index):
    chat = st.session_state.recent_chats[index]
    st.session_state.messages = chat["messages"].copy()
    st.session_state.chat_started = True
    st.session_state.input_key += 1
