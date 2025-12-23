import streamlit as st


def handle_new_chat_click():
    """
    Handles the 'New Chat' button click.

    - Saves the current chat into recent history (if messages exist)
    - Resets chat state for a fresh conversation
    """

    # Save current chat only if it contains messages
    if st.session_state.get("messages"):
        # Use the first user message as chat title (trimmed for sidebar display)
        title = st.session_state.messages[0]["content"][:30] + "..."

        # Insert at the top so the newest chat appears first
        st.session_state.recent_chats.insert(
            0,
            {
                "title": title,
                # Copy to prevent future mutations affecting saved chats
                "messages": st.session_state.messages.copy(),
            },
        )

        # Keep only the latest 10 chats to avoid memory/UI clutter
        st.session_state.recent_chats = st.session_state.recent_chats[:10]

    # Reset current chat state
    st.session_state.messages = []
    st.session_state.chat_started = False

    # Increment input_key to force Streamlit to re-render the input widget
    st.session_state.input_key += 1


def toggle_upload():
    """
    Toggles the file upload panel.

    When closing the uploader, the previously uploaded file is cleared
    to avoid using stale files in the next interaction.
    """

    st.session_state.upload_clicked = not st.session_state.upload_clicked

    # Clear file only when uploader is turned OFF
    if not st.session_state.upload_clicked:
        st.session_state.uploaded_file = None


def toggle_mic():
    """
    Toggles microphone listening state.

    A toast notification is shown to give immediate user feedback,
    which is important since mic state is not visually obvious.
    """

    st.session_state.mic_active = not st.session_state.mic_active

    st.toast(
        "🎙️ Microphone ON" if st.session_state.mic_active else "🔇 Microphone OFF"
    )


def load_chat(index: int):
    """
    Loads a previous chat from recent history.

    Parameters:
        index (int): Position of the chat in the recent_chats list.
    """

    chat = st.session_state.recent_chats[index]

    # Restore messages (copy avoids shared references)
    st.session_state.messages = chat["messages"].copy()

    # Mark chat as active so UI switches from landing state to chat view
    st.session_state.chat_started = True

    # Force input re-render to avoid stale text in input box
    st.session_state.input_key += 1
