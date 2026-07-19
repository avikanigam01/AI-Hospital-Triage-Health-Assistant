import joblib

from backend.preprocess import preprocess_input

# Load trained models
triage_model = joblib.load("data/triage_model.pkl")
department_model = joblib.load("data/department_model.pkl")


def predict(age,
            temperature,
            heart_rate,
            pain_level,
            symptom,
            duration):

    patient = preprocess_input(
        age,
        temperature,
        heart_rate,
        pain_level,
        symptom,
        duration
    )

    risk = triage_model.predict(patient)[0]

    department = department_model.predict(patient)[0]

    probability = max(triage_model.predict_proba(patient)[0])

    return {
        "risk": risk,
        "department": department,
        "confidence": round(probability * 100, 2)
    }