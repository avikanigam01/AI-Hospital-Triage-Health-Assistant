import pandas as pd
import joblib

# Load the trained LabelEncoder
encoder = joblib.load("data/encoder.pkl")


def preprocess_input(age, temperature, heart_rate, pain_level, symptom, duration):
    """
    Convert user input into a format suitable for the trained ML models.

    Parameters:
        age (int)
        temperature (float)
        heart_rate (int)
        pain_level (int)
        symptom (str)
        duration (int)

    Returns:
        pandas.DataFrame
    """

    # Clean the symptom input
    symptom = symptom.strip()

    # Encode the symptom safely
    try:
        symptom_encoded = encoder.transform([symptom])[0]
    except ValueError:
        raise ValueError(
            f"Unknown symptom: '{symptom}'. Please select a valid symptom from the list."
        )

    # Create model input
    patient = pd.DataFrame([
        {
            "Age": age,
            "Temperature_C": temperature,
            "Heart_Rate": heart_rate,
            "Pain_Level": pain_level,
            "Primary_Symptom": symptom_encoded,
            "Duration_Days": duration
        }
    ])

    return patient