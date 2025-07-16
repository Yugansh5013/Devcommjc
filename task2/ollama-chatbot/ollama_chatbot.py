import requests
import gradio as gr
import json
import pdfplumber
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
OLLAMA_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt, model="llava", history=[]):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "history": history,
            "stream": True
        },
        stream=True
    )

    reply = ""
    for line in response.iter_lines():
        if line:
            part = json.loads(line.decode("utf-8"))
            reply += part.get("response", "")
            yield reply


def extract_text_from_pdf(file):
    with pdfplumber.open(file.name) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text[:2000]  # limit prompt size


def extract_text_from_image(image: Image.Image) -> str:
    text = pytesseract.image_to_string(image)
    return text[:2000]


def multimodal_chat(message,history, image=None, file=None):
    if not message and not image and not file:
        yield "⚠️ Please provide a prompt, image, or file."
        return

    prompt = message or ""

    # If image is uploaded
    if image is not None:
        prompt += "\n\n[Image text extracted below:]\n"
        text = extract_text_from_image(image)
        prompt += text

    # If file is uploaded
    if file is not None:
        _, ext = os.path.splitext(file.name)
        if ext.lower().endswith(".pdf"):
            prompt += "\n\n[Text from PDF:]\n" + extract_text_from_pdf(file)
        elif ext.lower().endswith(".txt"):
            prompt += "\n\n[Text from file:]\n" + file.read().decode("utf-8")[:2000]
        else:
            yield "⚠️ Only PDF and TXT files are supported for now."
            return

    # Stream the output from Ollama
    for chunk in query_ollama(prompt, model="llava", history=history):  # or llama3
        yield chunk 


# --- Gradio Interface ---
chatbot_ui = gr.ChatInterface(
    multimodal_chat,
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(placeholder="Ask a question or upload a file/image...", lines=2),
    additional_inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.File(label="Upload PDF/TXT File")
    ],
    title="🧠 Local Ollama Chatbot with File & Image Support",
    description="This chatbot runs locally using Ollama and supports PDFs, images, and text prompts.",
)

if __name__ == "__main__":
    chatbot_ui.launch()
