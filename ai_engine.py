import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):

    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        return res.json().get("response", "")

    except Exception as e:
        return f"Error: {e}"