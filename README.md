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
```bash
git clone https://github.com/yourusername/CodeGenie.git
cd CodeGenie
