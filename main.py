import streamlit as st
from input_module import collect_patient_info
from symptom_module import extract_symptoms
from context_module import identify_missing_info
from prompt_module import build_medical_prompt
from analysis_module import analyze_symptoms
from question_module import generate_followup_questions
from safety_module import build_safety_guidance
from save_module import save_report, format_report
from utils import check_ollama

DISCLAIMER = """This AI-generated response is intended for educational and informational purposes only.
It is not a medical diagnosis and does not replace advice from a qualified healthcare professional.
For serious, worsening or urgent symptoms, seek appropriate medical care."""

st.set_page_config(page_title="AI Medical Symptom Assistant", page_icon="🩺", layout="wide")
st.title("AI-Powered Medical Symptom Assistant")
st.caption("Local AI powered by Ollama · Qwen3:4b")
st.warning("Informational support only — this app cannot diagnose conditions or replace a healthcare professional.")

with st.sidebar:
    st.header("Model settings")
    model = st.text_input("Ollama model", "qwen3:4b")
    if st.button("Check Ollama connection"):
        ok, message = check_ollama(model)
        st.success(message) if ok else st.error(message)

st.header("1. Patient information and symptoms")
patient, symptoms_text = collect_patient_info()

if patient and symptoms_text:
    st.subheader("Patient information")
    st.write({
        "Age": patient["age"], "Sex": patient["sex"],
        "Duration": patient["duration"], "Severity": patient["severity"],
        "Medical history": patient["history"] or "Not provided",
        "Medications": patient["medications"] or "Not provided",
        "Allergies": patient["allergies"] or "Not provided"
    })
    st.write("**Reported symptoms:**", symptoms_text)

    if st.button("Analyze symptoms", type="primary", use_container_width=True):
        try:
            with st.spinner("Extracting symptoms..."):
                extracted = extract_symptoms(symptoms_text, model)
            st.session_state["med_extracted"] = extracted
            with st.spinner("Checking for missing information..."):
                missing = identify_missing_info(patient, symptoms_text, model)
            st.session_state["med_missing"] = missing
            prompt = build_medical_prompt(patient, symptoms_text, extracted, missing)
            st.session_state["med_prompt"] = prompt
            with st.spinner("Generating preliminary informational analysis..."):
                analysis = analyze_symptoms(prompt, model)
            st.session_state["med_analysis"] = analysis
            with st.spinner("Generating follow-up questions..."):
                questions = generate_followup_questions(patient, symptoms_text, extracted, model)
            st.session_state["med_questions"] = questions
            st.session_state["med_guidance"] = build_safety_guidance(symptoms_text, analysis)
            st.session_state["med_patient"] = patient
            st.session_state["med_symptoms"] = symptoms_text
            st.success("Analysis completed.")
        except Exception as e:
            st.error(f"Analysis failed: {e}")
            st.info("Check Ollama is running and qwen3:4b is installed. If the model is slow, try a shorter symptom description.")

if "med_analysis" in st.session_state:
    st.divider()
    st.header("2. Structured symptom report")
    st.subheader("Reported symptoms")
    st.write(st.session_state.get("med_extracted", "Not available"))
    st.subheader("Patient information")
    st.json(st.session_state["med_patient"])
    st.subheader("Possible conditions and explanation")
    st.markdown(st.session_state["med_analysis"])
    st.subheader("Missing information")
    st.write(st.session_state.get("med_missing", "Not available"))
    st.subheader("Follow-up questions")
    st.markdown(st.session_state.get("med_questions", "Not available"))
    st.subheader("Medical attention guidance")
    st.warning(st.session_state.get("med_guidance", "If symptoms are severe, rapidly worsening, or concerning, seek appropriate professional medical care."))
    st.subheader("Disclaimer")
    st.info(DISCLAIMER)
    with st.expander("View constructed prompt"):
        st.code(st.session_state.get("med_prompt", ""), language="text")
    if st.button("Save report to outputs/medical_analysis.txt", use_container_width=True):
        try:
            path = save_report(st.session_state["med_patient"], st.session_state["med_symptoms"],
                st.session_state["med_extracted"], st.session_state["med_missing"],
                st.session_state["med_analysis"], st.session_state["med_questions"],
                st.session_state["med_guidance"], DISCLAIMER)
            st.success(f"Saved to {path}")
        except Exception as e:
            st.error(f"Could not save report: {e}")
    st.download_button("Download report", format_report(
        st.session_state["med_patient"], st.session_state["med_symptoms"],
        st.session_state["med_extracted"], st.session_state["med_missing"],
        st.session_state["med_analysis"], st.session_state["med_questions"],
        st.session_state["med_guidance"], DISCLAIMER),
        file_name="medical_analysis.txt", mime="text/plain")

st.divider()
st.caption("If you may be experiencing a medical emergency, contact local emergency services immediately. Do not wait for an AI response.")
