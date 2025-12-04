import streamlit as st
def inject_css():
    """Injects custom CSS styles for the application."""
    
    header_style = """
<style>
[data-testid="stHeader"] {
    padding-left: 0px !important;
    padding-right: 0px !important;
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}
.header {
	  display: flex;
	  justify-content: center;
	  align-items: center;
	#   padding: 16px;
	   margin-top: 0;
	#   margin-bottom: 0;
	  position: fixed; 
	  width: 600px;
      max-width: 90%; 
	#   top: 0;
	  z-index: 1000;
	#   background-color: #0e1117; 
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
/* FIX: Set sidebar width to 25vw (approx 1/4 of viewport width) */
[data-testid="stSidebar"] {
    max-width: 30vw; 
}
.top-section .middle-section .bottom-section {
  width: 100%; 
}
.sidebar-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.btn {
  text-align: left;
  background-color: #1e1e1e;
  margin-bottom: 12px;
  font-weight: 600;
  border-width: 0px;
  border-radius: 10px;
  color: #FFFFFF;
  height: 36px;
  padding-left: 10px;
  cursor: pointer;
}
.btn:hover {
  background-color: #9a9a9a;
}

/* Custom CSS to style Streamlit buttons to look like the original HTML buttons */
div[data-testid="stSidebar"] .stButton>button {
    text-align: left;
    background-color: #1e1e1e;
    margin-bottom: 12px;
    font-weight: 600;
    border-width: 0px;
    border-radius: 10px;
    color: #FFFFFF;
    height: 36px;
    padding-left: 10px;
    cursor: pointer;
    width: 100%; 
}
div[data-testid="stSidebar"] .stButton>button:hover {
    background-color: #9a9a9a;
}
h3 {
  color: #a0a0a0;
  font-size: 13px;
  font-weight: 500;
  margin: 16px 0 8px 4px;
}
.chat {
  border: none;
  color: #f1f1f1;
  text-align: left;
  padding: 8px;
  border-radius: 6px;
  width: 100%;
  cursor: pointer;
  margin-bottom: 6px;
}

/* Custom CSS for recent chat buttons (which are now Streamlit buttons) */
div[data-testid="stSidebar"] .middle-section .stButton>button {
    border: none;
    color: #f1f1f1;
    text-align: left;
    padding: 8px;
    border-radius: 6px;
    width: 100%;
    cursor: pointer;
    margin-bottom: 6px;
    background-color: transparent; 
    height: auto; 
    line-height: normal;
    font-weight: 400;
    padding-left: 0;
}
div[data-testid="stSidebar"] .middle-section .stButton>button:hover {
    background-color: #1f1f1f;
}
.chat:hover {
  background-color: #1f1f1f;
}
.bottom-section {
  border-top: 1px solid #2a2a2a;
  padding-top: 10px;
  margin-top: 12px;
}
.profile {
  display: flex;
  position: fixed;
  bottom: 20px;
  align-items: center;
  gap: 8px;
}
.avatar {
  background-color: #f56565;
  color: white;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
}
.details {
  flex: 1;
}
.name {
  font-size: 14px;
  font-weight: 600;
}
</style>
"""

    custom_css = """
<style>
/* Main app container */

[data-testid="stSidebarToggleButton"] {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1001; /* Ensure it stays above the header */
    margin: 8px; /* Add slight margin for aesthetics */
    border-radius: 5px;
}

.stApp 
{
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    padding: 0;
    transition: justify-content 0.5s ease-in-out;
}

.stApp.chat-started {
    justify-content: flex-start; 
}

	.main-content {
	    display: flex;
	    flex-direction: column;
	    align-items: center;
	    width: 100%;
	    flex-grow: 1; 
	    padding-top: 100px; /* Space for fixed header */
	    padding-bottom: 100px; /* Space for fixed input bar */
	    /* Remove padding-left: 25vw; to let Streamlit handle the main block width */
	}

/* Title element */
	.title {
	    font-size: 10px;
	    font-weight: 200;
	    margin-bottom: 2rem;
	    text-align: center;
	    opacity: 1;
	    visibility: visible;
	    position: absolute; /* Change to absolute to center within main-content */
	    top: 35%;
	    left: 50%;
	    transform: translate(-50%, -50%); /* Center it properly */
	    transition: opacity 0.5s ease-in-out, visibility 0.5s ease-in-out, height 0.5s ease-in-out;
	}

/* Title hidden when chat starts */
.title.hidden {
    opacity: 0;
    visibility: hidden;
    height: 0;
    margin: 0;
    padding: 0;
}

/* Chat History Container */
	.chat-history-container {
        position: fixed;
        height: calc(100vh - 90px); 
	    width: 800px;
	    max-width: 90%;
	    margin-top: 20px;
	    opacity: 0;
	    visibility: hidden;
	    transition: opacity 0.5s ease-in-out;
	    margin-left: auto;
	    margin-right: auto;
        overflow-y: auto;
	}

.chat-history-container.visible {
    opacity: 1;
    visibility: visible;
}

/* Message Styling */
.chat-message-row {
    display: flex;
    margin-bottom: 15px;
    padding: 0 10px;
}

.user-message-row {
    justify-content: flex-end;
}

.ai-message-row {
    justify-content: flex-start;
}

.chat-message-bubble {
    padding: 12px 18px;
    border-radius: 20px;
    max-width: 50%; 
    font-size: 1rem;
    line-height: 1.5;
    word-wrap: break-word;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.user-message-bubble {
    background-color: #005c4b; 
    color: white;
    border-bottom-right-radius: 4px;
}

.ai-message-bubble {
    background-color: #2c3e50; 
    color: white;
    border-bottom-left-radius: 4px;
}

/* Initial centered position */
.search-bar-container {
    position: fixed;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 30px;
    width: 600px;
    max-width: 90%;
    top: 45%;
    left: 50%;
    transform: translate(-50%, -50%);   /* Center horizontally + vertically */
    transition: all 0.4s ease-in-out;
}


.search-bar-container.fixed-bottom {
    position: fixed;
    bottom: 20px;
}


/* Icon Sizing: Target the buttons in the search bar */
.search-bar-container .stButton button {
    font-size: 1.5rem; 
    padding: 0 5px;
    margin: 0;
    line-height: 1; /* Ensure icons are centered vertically */
}

/* Ensure the input field itself is styled correctly within the container */
.stTextInput > div > div > input {
    background: transparent !important;
    border: none !important;
    outline: none !important;
    color: #f0f0f0 !important;
    font-size: 1.1rem !important;
    padding: 0 10px !important;
    flex-grow: 1;
}

.stTextInput label {
    display: none;
}

/* Hide Streamlit's default elements that interfere with the fixed bar */
#MainMenu, footer {
    visibility: hidden;
}

	.file-uploader-fixed {
	    position: fixed;
	    bottom: 100px; /* Position above the fixed-bottom search bar */
	    left: 50%;
	    transform: translateX(-50%);
	    width: 600px; /* Match search bar width */
	    max-width: 90%;
	    z-index: 99;
	    background-color: #1e1e1e;
	    padding: 15px;
	    border-radius: 10px;
	    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.5);
	}
</style>
"""
    st.markdown(header_style, unsafe_allow_html=True)
    st.markdown(side_bar_style, unsafe_allow_html=True)
    st.markdown(custom_css, unsafe_allow_html=True)





