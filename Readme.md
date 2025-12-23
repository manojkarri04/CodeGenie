# Code Genie

## Internship Experience

This repository contains work completed during my internship, where I developed
an AI-powered coding assistant using Streamlit and a locally hosted LLM via Ollama.
The focus was on real-time interaction, OCR processing, voice input, and clean UI
architecture following industry best practices.


**Code Genie** is an advanced, AI-powered conversational interface designed to provide seamless interaction with local Large Language Models (LLMs) via Ollama. It features a robust multi-modal input system, allowing users to interact through text, voice, and uploaded documents.

---

## 🚀 Features

### 🛠 Core Capabilities

* **Local LLM Integration:** Powered by **Ollama**, ensuring data privacy and low-latency responses by running models locally.
* **Real-time Streaming:** Token-by-token response streaming for a smooth, ChatGPT-like user experience.
* **Contextual Memory:** Maintains session-aware chat history for coherent long-form conversations.

### 📄 Multi-Modal Document Processing

The application includes a sophisticated OCR and document parsing engine that supports:

* **Images:** OCR processing via `EasyOCR` with automated grayscale conversion and downscaling for performance.
* **PDFs:** Text extraction using `pypdf`.
* **Office Suite:** Support for `.docx` (Word) and `.pptx` (PowerPoint) via `python-docx` and `python-pptx`.
* **Plain Text:** Standard `.txt` file ingestion.

### 🎙 Voice Intelligence

* **Speech-to-Text:** Integrated voice recognition using the Google Speech Recognition API.
* **Interactive Toggles:** Hands-free input capability with automated timeout and phrase limit handling.

### 🎨 Modern UI/UX

* **Responsive Design:** A polished, "dark-mode" aesthetic with custom CSS injection.
* **Sidebar Management:** Organized chat history and "New Chat" functionality to keep workspaces clean.
* **Dynamic Layout:** UI shifts seamlessly from a landing "search" state to an active "chat" state.

---

## 🏗 System Architecture

The application is built on a modular Python architecture designed for scalability and maintainability:

| Component | Responsibility |
| --- | --- |
| **`app.py`** | Main entry point, UI rendering, and session state management. |
| **`AppConfig`** | Centralized constants, API endpoints, and hardware constraints. |
| **`OCR Service`** | Handles multi-format file parsing and image-to-text conversion. |
| **`Ollama API`** | Manages asynchronous streaming communication with the local model. |
| **`Callbacks`** | Segregated logic for UI interactions (New chat, toggles, history loading). |

---

## 🛠 Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM Engine:** [Ollama](https://ollama.com/) (Running the `CodeGenie` model)
* **OCR:** [EasyOCR](https://github.com/JaidedAI/EasyOCR) & [PIL](https://www.google.com/search?q=https://python-pillow.org/)
* **Document Parsing:** `pypdf`, `python-docx`, `python-pptx`
* **Voice:** `SpeechRecognition`
* **Networking:** `Requests` (Streaming API calls)

---

## 📥 Installation & Setup

### 1. Prerequisites

* Python 3.9+
* [Ollama](https://ollama.com/) installed and running.
* A model named `CodeGenie` created in Ollama (or update `MODEL_NAME` in `AppConfig`).

### 2. Clone the Repository

```bash
git clone https://github.com/manojkarri04/CodeGenie.git
cd CodeGenie

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Application

```bash
streamlit run app.py

```

---

## ⚙️ Configuration

You can customize the application behavior within the `AppConfig` class in `app.py`:

* **`MAX_IMG_WIDTH`**: Adjust to balance OCR speed vs. accuracy.
* **`OLLAMA_URL`**: Update if your Ollama instance is hosted on a different server/port.
* **`VOICE_TIMEOUT`**: Change the duration the mic stays active without speech.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the OCR accuracy, add new document formats, or enhance the UI, feel free to fork the repo and submit a pull request.

---
