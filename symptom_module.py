from utils import ask_ollama

def extract_symptoms(text, model="qwen3:4b"):
    prompt = f"""Extract only symptoms explicitly reported by the user. Do not infer or diagnose.
Return a concise bullet list. If unclear, say "No clearly stated symptoms."
User text: {text}"""
    return ask_ollama(prompt, model, temperature=0.1, max_tokens=160)
