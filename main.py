from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from ai_engine import ask_ai
from brain import detect_mode
from rag_engine import get_context

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🏠 Home
@app.get("/", response_class=HTMLResponse)
def home():
    html_path = Path("templates/index.html")
    return HTMLResponse(html_path.read_text(encoding="utf-8"))

# 💬 Chat API
@app.get("/chat")
def chat(q: str):

    mode = detect_mode(q)

    context = get_context(q)

    if mode == "education":
        system = "You are a teacher. Explain in simple Hindi."
    elif mode == "health":
        system = "You are a health assistant. Give safe advice."
    elif mode == "farmer":
        system = "You are an agriculture expert."
    else:
        system = "Answer in Hindi."

    prompt = f"""
    {system}

    Context: {context}

    Question: {q}

    Answer in simple Hindi with steps.
    """

    response = ask_ai(prompt)

    return {
        "mode": mode,
        "context_used": context,
        "response": response
    }

# 🖼️ Image API (Multimodal 🔥)
@app.post("/image")
async def image_ai(file: UploadFile = File(...)):

    # simulate AI reasoning
    prompt = "This is a plant leaf image. Suggest disease and solution in Hindi."

    response = ask_ai(prompt)

    return {
        "response": response
    }