import streamlit as st

def collect_patient_info():
    with st.form("patient_form"):
        c1, c2 = st.columns(2)
        with c1:
            age = st.number_input("Age", min_value=0, max_value=120, value=22)
            sex = st.selectbox("Sex (optional)", ["Not specified", "Female", "Male", "Intersex", "Prefer not to say"])
            duration = st.text_input("Symptom duration", placeholder="e.g. 2 days")
            severity = st.selectbox("Self-reported severity", ["Mild", "Moderate", "Severe", "Unsure"])
        with c2:
            history = st.text_area("Relevant medical history (optional)", placeholder="Any relevant conditions")
            medications = st.text_input("Current medications (optional)")
            allergies = st.text_input("Allergies (optional)")
        symptoms = st.text_area("Describe your symptoms", height=150,
            placeholder="e.g. Fever, cough and sore throat for two days...")
        submitted = st.form_submit_button("Submit patient information")
    if submitted:
        if not symptoms.strip():
            st.error("Please describe the symptoms.")
            return None, None
        patient = {"age": int(age), "sex": sex, "duration": duration.strip(),
                   "severity": severity, "history": history.strip(),
                   "medications": medications.strip(), "allergies": allergies.strip()}
        st.session_state["submitted_patient"] = patient
        st.session_state["submitted_symptoms"] = symptoms.strip()
    return st.session_state.get("submitted_patient"), st.session_state.get("submitted_symptoms")
