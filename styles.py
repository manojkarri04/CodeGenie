# import streamlit as st

# def inject_css():
#     """Injects custom CSS styles for the application."""
    
#     header_style = """
# <style>
# [data-testid="stHeader"] {
#     padding: 0 !important;
# }

# .header {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     position: fixed;
#     width: 100%;
#     top: 0;
#     z-index: 1000;
#     background-color: #0e1117;
# }

# .logo {
#     color: #fff !important;
#     font-size: 24px;
#     font-weight: 400;
# }

# .share-button {
#     display: flex;
#     background-color: rgb(14, 17, 23);
#     color: #fff;
#     border-width: 0px;
#     align-items: center;
#     gap: 5px;
#     cursor: pointer;
#     padding: 8px 12px;
#     border-radius: 8px;
#     transition: background-color 0.2s;
# }

# .share-button:hover {
#     background-color: #333;
# }

# .share-button.hidden {
#     display: none !important;
# }
# </style>
# """

#     side_bar_style = """
# <style>
# [data-testid="stSidebar"] {
#     max-width: 280px;
#     min-width: 280px;
# }

# [data-testid="stSidebarNav"] {
#     padding-top: 2rem;
# }

# /* New Chat Button */
# div[data-testid="stSidebar"] .stButton>button {
#     text-align: left;
#     background-color: #1e1e1e;
#     margin-bottom: 12px;
#     font-weight: 600;
#     border: 1px solid #2a2a2a;
#     border-radius: 8px;
#     color: #FFFFFF;
#     height: 42px;
#     padding: 0 12px;
#     cursor: pointer;
#     width: 100%;
#     transition: all 0.2s ease;
# }

# div[data-testid="stSidebar"] .stButton>button:hover {
#     background-color: #2a2a2a;
#     border-color: #3a3a3a;
# }

# h3 {
#     color: #8e8ea0;
#     font-size: 12px;
#     font-weight: 600;
#     margin: 20px 0 8px 4px;
#     text-transform: uppercase;
#     letter-spacing: 0.5px;
# }

# /* Recent chat buttons */
# div[data-testid="stSidebar"] .stButton>button[key^="chat_load_btn"] {
#     border: none;
#     color: #ececf1;
#     text-align: left;
#     padding: 10px 12px;
#     border-radius: 8px;
#     width: 100%;
#     cursor: pointer;
#     margin-bottom: 4px;
#     background-color: transparent;
#     height: auto;
#     line-height: 1.4;
#     font-weight: 400;
#     transition: background-color 0.2s ease;
# }

# div[data-testid="stSidebar"] .stButton>button[key^="chat_load_btn"]:hover {
#     background-color: #2a2a2a;
# }

# .profile {
#     border-radius: 16px;
#     display: flex;
#     position: fixed;
#     bottom: 20px;
#     align-items: center;
#     gap: 12px;
#     padding: 10px 12px;
#     border-top: 1px solid #2a2a2a;
#     width: calc(260px - 2rem);
#     background-color: #0e1117;
# }

# .avatar {
#     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#     color: white;
#     width: 32px;
#     height: 32px;
#     border-radius: 50%;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     font-weight: 600;
#     font-size: 14px;
# }

# .details {
#     flex: 1;
# }

# .name {
#     font-size: 14px;
#     font-weight: 600;
#     color: #ececf1;
# }
# </style>
# """

#     custom_css = """
# <style>
# /* Hide Streamlit default elements */
# #MainMenu, footer, .stDeployButton {
#     visibility: hidden;
#     display: none;
# }

# [data-testid="stSidebarToggleButton"] {
#     position: fixed;
#     top: 10px;
#     left: 10px;
#     z-index: 1001;
# }

# /* Main app container */
# .stApp {
#     color: #ececf1;
#     background-color: #0e1117;
# }

# /* Main content area */
# .main .block-container {
#     padding-top: 2rem;
#     padding-bottom: 120px;
#     max-width: 48rem;
# }

# /* Title - centered initially, above text box */
# .title {
#     font-size: 32px;
#     font-weight: 600;
#     text-align: center;
#     color: #ececf1;
#     margin-bottom: 2rem;
#     position: fixed;
#     top: 50%;
#     left: 61%;
#     transform: translate(-50%, -180%);
#     z-index: 1;
#     opacity: 1;
#     transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
#     white-space: nowrap;
# }

# .title.hidden {
#     opacity: 0;
#     pointer-events: none;
#     transform: translate(-50%, -200%);
# }

# /* Chat History Container */
# .chat-history-container {
#     width: 100%;
#     max-width: 48rem;
#     margin: 0 auto;
#     padding: 0 1rem 120px 1rem;
#     opacity: 0;
#     transition: opacity 0.3s ease-in-out;
# }

# .chat-history-container.visible {
#     opacity: 1;
# }

# /* Message Styling */
# .chat-message-row {
#     display: flex;
#     margin-bottom: 24px;
#     width: 100%;
# }

# .user-message-row {
#     justify-content: flex-end;
# }

# .ai-message-row {
#     justify-content: flex-start;
# }

# .chat-message-bubble {
#     padding: 12px 16px;
#     border-radius: 18px;
#     max-width: 70%;
#     font-size: 15px;
#     line-height: 1.6;
#     word-wrap: break-word;
#     box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
# }

# .chat-message-bubble ai-message-row {
#    animation:
#    typing 2s steps(15),
#    cursor .4s step-end infinite alternate;
# }
# .user-message-bubble {
#     background-color: #2f2f2f;
#     color: #ececf1;
#     border-bottom-right-radius: 4px;
# }

# .ai-message-bubble {
#     background-color: #1e1e1e;
#     color: #ececf1;
#     border-bottom-left-radius: 4px;
# }

# /* Search bar container - centered initially, fixed at bottom after chat starts */
# .search-bar-container {
#     position: fixed;
#     bottom: 50%;
#     left: 50%;
#     transform: translate(-50%, 50%);
#     width: 100%;
#     max-width: 48rem;
#     padding: 0 1rem;
#     z-index: 100;
#     transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
# }

# .search-bar-container.fixed-bottom {
#     bottom: 0;
#     transform: translate(-50%, 0);
#     padding: 1.5rem 1rem;
#     background: linear-gradient(to top, #0e1117 80%, transparent);
# }

# /* Input wrapper */
# .search-bar-container > div[data-testid="column"] {
#     display: flex;
#     align-items: flex-end;
# }

# /* Hide text area label */
# .search-bar-container .stTextArea label {
#     display: none;
# }

# /* Text area styling */
# .search-bar-container .stTextArea {
#     flex: 1;
#     margin: 0 8px;
# }

# .search-bar-container .stTextArea textarea {
#     background-color: #2f2f2f !important;
#     border: 1px solid #424242 !important;
#     border-radius: 24px !important;
#     color: #ececf1 !important;
#     font-size: 15px !important;
#     padding: 14px 20px !important;
#     resize: none !important;
#     min-height: 52px !important;
#     max-height: 200px !important;
#     line-height: 1.5 !important;
#     box-shadow: 0 0 0 0 transparent !important;
#     transition: border-color 0.2s ease, background-color 0.2s ease !important;
# }

# .search-bar-container .stTextArea textarea:focus {
#     background-color: #353535 !important;
#     border-color: #565869 !important;
#     outline: none !important;
#     box-shadow: 0 0 0 3px rgba(86, 88, 105, 0.1) !important;
# }

# .search-bar-container .stTextArea textarea::placeholder {
#     color: #8e8ea0 !important;
# }

# /* Button styling in search bar */
# .search-bar-container .stButton button {
#     background-color: transparent !important;
#     border: none !important;
#     color: #8e8ea0 !important;
#     font-size: 20px !important;
#     padding: 0 !important;
#     width: 44px !important;
#     height: 44px !important;
#     min-width: 44px !important;
#     min-height: 44px !important;
#     max-width: 44px !important;
#     max-height: 44px !important;
#     border-radius: 50% !important;
#     transition: all 0.2s ease !important;
#     cursor: pointer !important;
#     display: flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     line-height: 1 !important;
# }

# .search-bar-container .stButton button:hover {
#     background-color: #2a2a2a !important;
#     color: #ececf1 !important;
# }

# .search-bar-container .stButton button:active {
#     transform: scale(0.95);
# }

# /* File uploader styling */
# .file-uploader-fixed {
#     position: fixed;
#     bottom: 90px;
#     left: 50%;
#     transform: translateX(-50%);
#     width: 100%;
#     max-width: 48rem;
#     padding: 0 1rem;
#     z-index: 99;
# }

# .file-uploader-fixed .stFileUploader {
#     background-color: #2f2f2f;
#     border: 1px solid #424242;
#     border-radius: 12px;
#     padding: 16px;
#     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
# }

# .file-uploader-fixed .stFileUploader label {
#     color: #ececf1 !important;
#     font-weight: 500;
# }

# /* Expander styling */
# .stExpander {
#     background-color: #1e1e1e;
#     border: 1px solid #2a2a2a;
#     border-radius: 8px;
#     margin-top: 12px;
# }

# .stExpander summary {
#     color: #ececf1;
#     font-weight: 500;
# }

# /* Text area inside expander */
# .stExpander .stTextArea textarea {
#     background-color: #0e1117 !important;
#     border: 1px solid #2a2a2a !important;
#     color: #ececf1 !important;
#     font-family: 'Monaco', 'Menlo', monospace !important;
#     font-size: 13px !important;
# }

# /* Toast notifications */
# .stToast {
#     background-color: #2f2f2f !important;
#     color: #ececf1 !important;
#     border: 1px solid #424242 !important;
# }

# /* Scrollbar styling */
# ::-webkit-scrollbar {
#     width: 8px;
#     height: 8px;
# }

# ::-webkit-scrollbar-track {
#     background: #1e1e1e;
# }

# ::-webkit-scrollbar-thumb {
#     background: #424242;
#     border-radius: 4px;
# }

# ::-webkit-scrollbar-thumb:hover {
#     background: #565869;
# }

# /* Responsive design */
# @media (max-width: 768px) {
#     .title {
#         font-size: 24px;
#     }
    
#     .chat-message-bubble {
#         max-width: 85%;
#         font-size: 14px;
#     }
    
#     .search-bar-container {
#         max-width: 100%;
#     }
# }
# </style>
# """

#     st.markdown(header_style, unsafe_allow_html=True)
#     st.markdown(side_bar_style, unsafe_allow_html=True)
#     st.markdown(custom_css, unsafe_allow_html=True)

import streamlit as st

def inject_css():
    """Injects custom CSS styles for the application."""
    
    header_style = """
<style>
[data-testid="stHeader"] {
    padding: 0 !important;
}

.header {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    background-color: #0e1117;
}

.logo {
    color: #fff !important;
    font-size: 24px;
    font-weight: 400;
}

.share-button {
    display: flex;
    background-color: rgb(14, 17, 23);
    color: #fff;
    border-width: 0px;
    align-items: center;
    gap: 5px;
    cursor: pointer;
    padding: 8px 12px;
    border-radius: 8px;
    transition: background-color 0.2s;
}

.share-button:hover {
    background-color: #333;
}

.share-button.hidden {
    display: none !important;
}
</style>
"""

    side_bar_style = """
<style>
[data-testid="stSidebar"] {
    max-width: 300px;
    min-width: 300px;
}

[data-testid="stSidebarNav"] {
    padding-top: 2rem;
}

/* New Chat Button */
div[data-testid="stSidebar"] .stButton>button {
    text-align: left;
    background-color: #1e1e1e;
    margin-bottom: 12px;
    font-weight: 600;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    color: #FFFFFF;
    height: 42px;
    padding: 0 12px;
    cursor: pointer;
    width: 100%;
    transition: all 0.2s ease;
}

div[data-testid="stSidebar"] .stButton>button:hover {
    background-color: #2a2a2a;
    border-color: #3a3a3a;
}

h3 {
    color: #8e8ea0;
    font-size: 12px;
    font-weight: 600;
    margin: 20px 0 8px 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Recent chat buttons */
div[data-testid="stSidebar"] .stButton>button[key^="chat_load_btn"] {
    border: none;
    color: #ececf1;
    text-align: left;
    padding: 10px 12px;
    border-radius: 8px;
    width: 100%;
    cursor: pointer;
    margin-bottom: 4px;
    background-color: transparent;
    height: auto;
    line-height: 1.4;
    font-weight: 400;
    transition: background-color 0.2s ease;
}

div[data-testid="stSidebar"] .stButton>button[key^="chat_load_btn"]:hover {
    background-color: #2a2a2a;
}

.profile {
    border-radius: 16px;
    display: flex;
    position: fixed;
    bottom: 20px;
    align-items: center;
    gap: 12px;
    padding: 10px 12px;
    border-top: 1px solid #2a2a2a;
    width: calc(260px - 2rem);
    background-color: #0e1117;
}

.avatar {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 600;
    font-size: 14px;
}

.details {
    flex: 1;
}

.name {
    font-size: 14px;
    font-weight: 600;
    color: #ececf1;
}
</style>
"""

    custom_css = """
<style>
/* Hide Streamlit default elements */
#MainMenu, footer, .stDeployButton {
    visibility: hidden;
    display: none;
}

[data-testid="stSidebarToggleButton"] {
    position: fixed;
    top: 10px;
    left: 10px;
    z-index: 1001;
}

/* Main app container */
.stApp {
    color: #ececf1;
    background-color: #0e1117;
}

/* Main content area */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 120px;
    max-width: 48rem;
}

/* --- NEW CSS FOR TYPING EFFECT ALIGNMENT --- */
/* This targets the st.empty() placeholder created by the typewriter_effect 
   to ensure its width matches the chat history container. */
.main .block-container > div:last-child > div:nth-last-child(4) > div:first-child > div:first-child {
    max-width: 48rem;
    margin: 0 auto;
    padding: 0 1rem;
}
/* --- END NEW CSS --- */


/* Title - centered initially, above text box */
.title {
    font-size: 32px;
    font-weight: 600;
    text-align: center;
    color: #ececf1;
    margin-bottom: 2rem;
    position: fixed;
    top: 50%;
    left: 61%;
    transform: translate(-50%, -180%);
    z-index: 1;
    opacity: 1;
    transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
    white-space: nowrap;
}

.title.hidden {
    opacity: 0;
    pointer-events: none;
    transform: translate(-50%, -200%);
}

/* Chat History Container */
.chat-history-container {
    width: 100%;
    max-width: 48rem;
    margin: 0 auto;
    padding: 0 1rem 120px 1rem;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
}

.chat-history-container.visible {
    opacity: 1;
}

/* Message Styling */
.chat-message-row {
    display: flex;
    margin-bottom: 24px;
    width: 100%;
}

.user-message-row {
    justify-content: flex-end;
}

.ai-message-row {
    justify-content: flex-start;
}

.chat-message-bubble {
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 70%;
    font-size: 15px;
    line-height: 1.6;
    word-wrap: break-word;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

/* Note: Removed the unused typing animation keyframes from the original styles */

.user-message-bubble {
    background-color: #2f2f2f;
    color: #ececf1;
    border-bottom-right-radius: 4px;
}

.ai-message-bubble {
    background-color: #1e1e1e;
    color: #ececf1;
    border-bottom-left-radius: 4px;
}

/* Search bar container - centered initially, fixed at bottom after chat starts */
.search-bar-container {
    position: fixed;
    bottom: 50%;
    left: 50%;
    transform: translate(-50%, 50%);
    width: 100%;
    max-width: 48rem;
    padding: 0 1rem;
    z-index: 100;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.search-bar-container.fixed-bottom {
    bottom: 0;
    transform: translate(-50%, 0);
    padding: 1.5rem 1rem;
    background: linear-gradient(to top, #0e1117 80%, transparent);
}

/* Input wrapper */
.search-bar-container > div[data-testid="column"] {
    display: flex;
    align-items: flex-end;
}

/* Hide text area label */
.search-bar-container .stTextArea label {
    display: none;
}

/* Text area styling */
.search-bar-container .stTextArea {
    flex: 1;
    margin: 0 8px;
}

.search-bar-container .stTextArea textarea {
    background-color: #2f2f2f !important;
    border: 1px solid #424242 !important;
    border-radius: 24px !important;
    color: #ececf1 !important;
    font-size: 15px !important;
    padding: 14px 20px !important;
    resize: none !important;
    min-height: 52px !important;
    max-height: 200px !important;
    line-height: 1.5 !important;
    box-shadow: 0 0 0 0 transparent !important;
    transition: border-color 0.2s ease, background-color 0.2s ease !important;
}

.search-bar-container .stTextArea textarea:focus {
    background-color: #353535 !important;
    border-color: #565869 !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(86, 88, 105, 0.1) !important;
}

.search-bar-container .stTextArea textarea::placeholder {
    color: #8e8ea0 !important;
}

/* Button styling in search bar */
.search-bar-container .stButton button {
    background-color: transparent !important;
    border: none !important;
    color: #8e8ea0 !important;
    font-size: 20px !important;
    padding: 0 !important;
    width: 44px !important;
    height: 44px !important;
    min-width: 44px !important;
    min-height: 44px !important;
    max-width: 44px !important;
    max-height: 44px !important;
    border-radius: 50% !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1 !important;
}

.search-bar-container .stButton button:hover {
    background-color: #2a2a2a !important;
    color: #ececf1 !important;
}

.search-bar-container .stButton button:active {
    transform: scale(0.95);
}

/* File uploader styling */
.file-uploader-fixed {
    position: fixed;
    bottom: 90px;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 48rem;
    padding: 0 1rem;
    z-index: 99;
}

.file-uploader-fixed .stFileUploader {
    background-color: #2f2f2f;
    border: 1px solid #424242;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.file-uploader-fixed .stFileUploader label {
    color: #ececf1 !important;
    font-weight: 500;
}

/* Expander styling */
.stExpander {
    background-color: #1e1e1e;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    margin-top: 12px;
}

.stExpander summary {
    color: #ececf1;
    font-weight: 500;
}

/* Text area inside expander */
.stExpander .stTextArea textarea {
    background-color: #0e1117 !important;
    border: 1px solid #2a2a2a !important;
    color: #ececf1 !important;
    font-family: 'Monaco', 'Menlo', monospace !important;
    font-size: 13px !important;
}

/* Toast notifications */
.stToast {
    background-color: #2f2f2f !important;
    color: #ececf1 !important;
    border: 1px solid #424242 !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #1e1e1e;
}

::-webkit-scrollbar-thumb {
    background: #424242;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #565869;
}

/* Responsive design */
@media (max-width: 768px) {
    .title {
        font-size: 24px;
    }
    
    .chat-message-bubble {
        max-width: 85%;
        font-size: 14px;
    }
    
    .search-bar-container {
        max-width: 100%;
    }
}
</style>
"""

    st.markdown(header_style, unsafe_allow_html=True)
    st.markdown(side_bar_style, unsafe_allow_html=True)
    st.markdown(custom_css, unsafe_allow_html=True)