# AI-Powered Medical Symptom Assistant — Qwen3:4b

Educational Streamlit app using local Ollama to extract reported symptoms, identify missing context, provide broad possible causes, generate follow-up questions, and save a structured report.

## Setup (Windows PowerShell)
```powershell
ollama pull qwen3:4b
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run main.py
```

Keep Ollama running at `http://localhost:11434`.

## Safety
This is not a medical device and does not provide diagnosis or treatment. AI output may be incorrect. Seek emergency care for urgent symptoms and consult a qualified healthcare professional for personal medical advice.
