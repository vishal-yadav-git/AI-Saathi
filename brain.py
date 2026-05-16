def detect_mode(query):
    q = query.lower()

    if any(w in q for w in ["class", "math", "study"]):
        return "education"
    elif any(w in q for w in ["bukhar", "fever", "pain"]):
        return "health"
    elif any(w in q for w in ["kheti", "fasal", "crop"]):
        return "farmer"
    else:
        return "general"