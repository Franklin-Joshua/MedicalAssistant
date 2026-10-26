from utils import ask_ollama

def generate_followup_questions(patient, symptoms, extracted, model="qwen3:4b"):
    prompt = f"""Suggest up to 5 concise follow-up questions for a general symptom information conversation.
Prioritize severity, onset/progression, and urgent warning signs relevant to the reported symptoms.
Do not delay urgent care to answer these questions. Do not diagnose.
Patient: {patient}
Symptoms: {symptoms}
Extracted symptoms: {extracted}
Return a numbered list only."""
    return ask_ollama(prompt, model, temperature=0.1, max_tokens=220)
