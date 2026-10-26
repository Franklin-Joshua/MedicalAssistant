import os
from datetime import datetime

def format_report(patient, symptoms, extracted, missing, analysis, questions, guidance, disclaimer):
    return f"""AI-POWERED MEDICAL SYMPTOM ASSISTANT
Generated: {datetime.now():%Y-%m-%d %H:%M:%S}

PATIENT INFORMATION
{patient}

USER-REPORTED SYMPTOMS
{symptoms}

EXTRACTED SYMPTOMS
{extracted}

MISSING INFORMATION
{missing}

SYMPTOM ANALYSIS
{analysis}

FOLLOW-UP QUESTIONS
{questions}

MEDICAL ATTENTION GUIDANCE
{guidance}

DISCLAIMER
{disclaimer}

{'-'*70}
"""

def save_report(patient, symptoms, extracted, missing, analysis, questions, guidance, disclaimer):
    os.makedirs("outputs", exist_ok=True)
    path = os.path.join("outputs", "medical_analysis.txt")
    with open(path, "a", encoding="utf-8") as f:
        f.write(format_report(patient, symptoms, extracted, missing, analysis, questions, guidance, disclaimer))
    return path
