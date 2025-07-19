# Ollama Local Chatbot with Multimodal Support

This project is a **fully offline AI chatbot** powered by [Ollama](https://ollama.com), running large language models like `llama3` and `llava` locally on your machine. It features:

* Text chat using LLMs (llama3/llava)
* Image input with OCR (text extraction)
* PDF and TXT file upload + parsing
* Real-time streaming chat
* Clean and interactive web UI (Gradio)

* 100% local, private, and secure     
---

## Features                                                                                          

| Feature                     | Description                                         |
| --------------------------- | --------------------------------------------------- |
| Text Chat                   | Ask anything using llama3 or llava locally          |
| Image Upload (OCR)          | Upload image and extract text using Tesseract OCR   |
| PDF + TXT Upload            | Upload and extract content from PDFs and .txt files |
| Streamed Responses          | Get LLM output token-by-token in real-time          |
| Error Handling              | Handles invalid inputs, model not running, timeouts |
| Offline Capability          | No internet needed after downloading Ollama models  |
| Customizable Prompt Builder | Combines user input + file/image text for LLM       |

---

## Requirements

> Make sure Python 3.10+ and Ollama are installed.

### Python Libraries

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, manually install:

```bash
pip install gradio requests pdfplumber pytesseract pillow
```

### Install Ollama

Follow the instructions at: [https://ollama.com/download](https://ollama.com/download)

```bash
# Example for Windows/macOS/Linux
ollama run llama3
ollama run llava
```

### Install Tesseract OCR (for image input)

* Download for Windows: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
* Install to:

  ```
  C:\Program Files\Tesseract-OCR
  ```
* Add to your environment `PATH`
* In code, specify:

  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
  ```

---

## How to Run the App

### 1. Start Ollama Model (in separate terminal)

```bash
ollama run llama3  # For text
ollama run llava   # For images + text
```

### 2. Run the Web App

```bash
python ollama_chatbot.py
```

You will see a local URL:

```
Running on http://127.0.0.1:7860
```

Open this in your browser.

---

## Author

Made by \[Your Name] as part of DevComm JC Task 2

---

> "AI should be private, powerful, and yours. This chatbot makes it real."
