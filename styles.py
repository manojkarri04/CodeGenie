import streamlit as st


def inject_css():
    """
    Injects all custom CSS required for the ChatGPT-style Streamlit UI.
    Unnecessary, duplicate, and fragile selectors have been removed.
    """

    # ---------------- HEADER ----------------
    # Removes default padding and applies dark background
    header_css = """
    <style>
    [data-testid="stHeader"] {
        background-color: #010409;
        padding: 0 !important;
    }
    </style>
    """

    # ---------------- SIDEBAR ----------------
    # Fixed-width sidebar with dark theme
    sidebar_css = """
    <style>
    [data-testid="stSidebar"] {
        min-width: 320px;
        max-width: 320px;
        background-color: #010409;
    }

    /* Hide Streamlit deploy button */
    .stDeployButton {
        display: none !important;
    }

    /* Sidebar buttons (New Chat / History) */
    div[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        height: 42px;
        background-color: #010409;
        border: 1px solid #2a2a2a;
        border-radius: 8px;
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 10px;
        transition: background-color 0.2s ease;
    }

    div[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #161B22;
    }

    /* Profile section fixed at bottom */
    .profile-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 320px;
        height: 76px;
        display: flex;
        align-items: center;
        gap:10px;
        padding: 20px;
        background-color: #0D1117;
        border-top-right-radius:24px;
        border-top: 1px solid #2a2a2a;
        z-index: 100;
    }

    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        justify-content:center;
        align-items:center;
        font-size:14px;
        dispay:flex;
        background-color: #0000FF;
    }

    .name {
        color: #ececf1;
        font-size: 14px;
        font-weight: 600;
    }
    </style>
    """

    # ---------------- MAIN APP ----------------
    # Core app layout, chat UI, input box, and responsiveness
    main_css = """
    <style>

    /* Remove Streamlit default UI */
    #MainMenu, footer {
        display: none;
    }

    /* App background */
    .stApp {
        background-color: #0D1117;
        color: #ececf1;
    }

    /* Main container width & spacing */
    .main .block-container {
        max-width: 48rem;
        padding-top: 2rem;
        padding-bottom: 150px;
    }

    /* -------- TITLE (Landing Screen) -------- */
    .title {
        position: fixed;
        top: 50%;
        left: 60%;
        transform: translate(-50%, -180%);
        font-size: 32px;
        font-weight: 600;
        text-align: center;
        transition: opacity 0.3s ease;
    }

    .title.hidden {
        opacity: 0;
        pointer-events: none;
    }

    /* -------- CHAT HISTORY -------- */
    .chat-history-container {
        max-width: 48rem;
        margin: 0 auto;
        padding: 0 1rem 120px;
    }

    .chat-message-row {
        display: flex;
        margin-bottom: 24px;
    }

    .user-message-row {
        justify-content: flex-end;
    }

    .ai-message-row {
        justify-content: flex-start;
    }

    .chat-message-bubble {
        max-width: 70%;
        padding: 12px 16px;
        border-radius: 18px;
        font-size: 15px;
        line-height: 1.6;
    }

    .user-message-bubble {
        background-color: #238636;
        color: #ECFDF5;
        border-bottom-right-radius: 4px;
    }

    .ai-message-bubble {
        background-color: #161B22;
        color: #C9D1D9;
        border-bottom-left-radius: 4px;
    }

    /* -------- TYPING EFFECT CONTAINER -------- */
    /* Use this class in Python instead of fragile DOM selectors */
    .typing-container {
        max-width: 48rem;
        margin: 0 auto;
        padding: 0 1rem;
    }

    /* -------- INPUT BAR -------- */
    .search-bar-container {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        max-width: 48rem;
        padding: 1.5rem 1rem;
        background: linear-gradient(to top, #0e1117 80%, transparent);
        z-index: 100;
    }

    .search-bar-container textarea {
        background-color: #2f2f2f !important;
        border: 1px solid #424242 !important;
        border-radius: 24px !important;
        color: #ececf1 !important;
        padding: 14px 20px !important;
        resize: none !important;
    }

    /* -------- FILE UPLOADER -------- */
    .file-uploader-fixed {
        position: fixed;
        bottom: 90px;
        left: 50%;
        transform: translateX(-50%);
        max-width: 48rem;
        width: 100%;
        padding: 0 1rem;
        z-index: 99;
    }

    /* -------- SCROLLBAR -------- */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {
        background: #424242;
        border-radius: 4px;
    }

    /* -------- RESPONSIVE -------- */
    @media (max-width: 768px) {
        .title {
            font-size: 24px;
        }

        .chat-message-bubble {
            max-width: 85%;
            font-size: 14px;
        }
    }

    </style>
    """

    # Inject styles
    st.markdown(header_css, unsafe_allow_html=True)
    st.markdown(sidebar_css, unsafe_allow_html=True)
    st.markdown(main_css, unsafe_allow_html=True)
