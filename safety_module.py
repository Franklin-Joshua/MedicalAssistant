def build_safety_guidance(symptoms, analysis):
    # Conservative fixed guidance; not a clinical triage model.
    return (
        "This app cannot determine whether a symptom is safe to monitor at home. "
        "Seek urgent/emergency care now for severe difficulty breathing, chest pain, "
        "new confusion, fainting, blue/grey lips, signs of stroke, severe bleeding, "
        "or any rapidly worsening or otherwise alarming symptoms. For persistent, "
        "worsening, or concerning symptoms, contact a qualified healthcare professional. "
        "Do not delay urgent care to use this tool."
    )
