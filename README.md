# CodeGenie
# 🧠 CodeGenie – AI Chat Assistant with OCR, Voice Input & Document Processing

CodeGenie is an advanced AI-powered chat assistant built using **Streamlit**, **Ollama**, and **EasyOCR**.  
It allows users to interact using text, voice, or by uploading documents such as **PDFs, images, DOCX, and text files**.  
The system extracts content from uploaded files using OCR and provides intelligent responses using locally hosted LLMs.

---

## 🚀 Features

### 💬 Intelligent Chat Interface
- Fully functional chat UI built with Streamlit
- Supports dynamic message rendering for both user and AI responses
- Maintains chat history using session state

### 🎙️ Voice Input (Speech-to-Text)
- Speak directly to the assistant
- Uses `speech_recognition` + Google Web Speech API
- Auto-converts speech to text and submits to the model

### 📄 OCR + Document Understanding
Supports extracting text from:
- 🖼️ Images (PNG, JPG, JPEG)
- 📄 PDF files
- 📝 TXT files
- 📘 DOCX documents

Uses `EasyOCR` for image extraction and native libraries for text formats.

### 🤖 LLM Integration (Ollama)
- Works with **Ollama local models** (default: `llama3.2`)
- Sends queries and extracted text to the model for analysis, explanation, or summarization

### 📎 File Upload System
- Floating file upload interface
- Auto-preview extracted text
- Optional full-text expander

### 🎨 Custom UI/UX
- Sidebar with recent chats
- Custom header branding
- Floating chat input bar
- Clean and responsive styling

---

## 📦 Installation

### 1. Clone the Repository
git clone https://github.com/yourusername/CodeGenie.git
cd CodeGenie

Create a Virtual Environment

python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

Install Dependencies

pip install -r requirements.txt

▶️ Running the App

streamlit run app.py

📙 Folder Structure

streamlit-project/
│── project.py           # Main Streamlit application
│── callbacks.py         # All UI event handlers
│── styles.py            # Custom CSS injection
│── README.md            # Documentation
│── requirements.txt     # Python dependencies

🧩 Technologies Used
Component	      Library / Tech
UI	            Streamlit
OCR	            EasyOCR
PDF	            pypdf
DOCX	          python-docx
Voice Input	    SpeechRecognition
LLM Backend	    Ollama
HTTP Requests	  requests
Image Handling	Pillow, NumPy

🛠️ Troubleshooting

pip install easyocr
pip install opencv-python-headless

📄 License

MIT License © 2025
