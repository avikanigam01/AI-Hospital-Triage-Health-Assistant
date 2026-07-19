import pandas as pd
import joblib

# Load encoder
encoder = joblib.load("data/encoder.pkl")


def preprocess_input(age, temperature, heart_rate, pain_level, symptom, duration):
    """
    Convert user input into model-ready format.
    """

    # Encode symptom
    symptom = encoder.transform([symptom])[0]

    patient = pd.DataFrame(
        [{
            "Age": age,
            "Temperature_C": temperature,
            "Heart_Rate": heart_rate,
            "Pain_Level": pain_level,
            "Primary_Symptom": symptom,
            "Duration_Days": duration
        }]
    )

    return patient