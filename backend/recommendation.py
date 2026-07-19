recommendations = {
    "Emergency": {
        "color": "red",
        "seek_care": "Go to the nearest Emergency Department immediately.",
        "first_aid": [
            "Stay calm and avoid unnecessary movement.",
            "Call emergency services if symptoms are severe.",
            "Do not delay seeking medical care."
        ]
    },

    "Urgent": {
        "color": "orange",
        "seek_care": "Visit a doctor or hospital as soon as possible.",
        "first_aid": [
            "Stay hydrated.",
            "Monitor your symptoms carefully.",
            "Avoid strenuous activity until evaluated."
        ]
    },

    "Routine": {
        "color": "green",
        "seek_care": "Schedule a regular consultation with your doctor.",
        "first_aid": [
            "Rest adequately.",
            "Drink plenty of fluids.",
            "Monitor symptoms and seek care if they worsen."
        ]
    }
}


def get_recommendation(prediction):
    """
    prediction is the dictionary returned by predictor.py
    """

    risk = prediction["risk"]

    department = prediction["department"]

    recommendation = recommendations[risk]

    return {
        "risk": risk,
        "department": department,
        "confidence": prediction["confidence"],
        "color": recommendation["color"],
        "seek_care": recommendation["seek_care"],
        "first_aid": recommendation["first_aid"]
    }