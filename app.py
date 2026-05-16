import requests

def ask_ai(prompt):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma",
            "prompt": prompt,
            "stream": False
        }
    )
    return res.json()["response"]

while True:
    user = input("You: ")
    print("AI:", ask_ai(user))
