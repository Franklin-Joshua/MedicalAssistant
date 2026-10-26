from utils import ask_ollama

def identify_missing_info(patient, symptoms, model="qwen3:4b"):
    prompt = f"""List relevant information that is missing or unclear for a general symptom discussion.
Do not ask for identifying information and do not assume facts.
Patient details: {patient}
Reported symptoms: {symptoms}
Return at most 5 concise bullets. If no useful gaps, say so."""
    return ask_ollama(prompt, model, temperature=0.1, max_tokens=180)
