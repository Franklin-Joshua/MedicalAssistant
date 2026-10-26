from utils import ask_ollama

def analyze_symptoms(prompt, model="qwen3:4b"):
    return ask_ollama(prompt, model, temperature=0.1, max_tokens=650)
