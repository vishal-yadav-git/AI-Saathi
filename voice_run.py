from voice import listen
from tts import speak
from ai_engine import ask_ai

while True:
    user = listen()

    if user:
        response = ask_ai(user)
        print("AI:", response)
        speak(response)