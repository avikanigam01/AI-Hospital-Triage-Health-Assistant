import pandas as pd
import joblib
import os

print(os.getcwd())

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/AI_Hospital_Triage_Dataset.csv")

# Encode symptom
encoder = LabelEncoder()
df["Primary_Symptom"] = encoder.fit_transform(df["Primary_Symptom"])

# Features
X = df[
    [
        "Age",
        "Temperature_C",
        "Heart_Rate",
        "Pain_Level",
        "Primary_Symptom",
        "Duration_Days",
    ]
]

# Target 1
y_triage = df["Triage_Level"]

# Target 2
y_department = df["Recommended_Department"]

# Train Triage Model
triage_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

triage_model.fit(X, y_triage)

# Train Department Model
department_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

department_model.fit(X, y_department)

# Save everything
joblib.dump(triage_model, "data/triage_model.pkl")
joblib.dump(department_model, "data/department_model.pkl")
joblib.dump(encoder, "data/encoder.pkl")

print("Both models trained successfully!")