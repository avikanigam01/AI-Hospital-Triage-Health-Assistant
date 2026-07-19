def generate_reason(age, temperature, heart_rate, pain_level, duration):

    reasons = []

    if temperature >= 39:
        reasons.append("High body temperature detected.")

    if heart_rate >= 110:
        reasons.append("Elevated heart rate.")

    if pain_level >= 8:
        reasons.append("Severe pain reported.")

    if age >= 65:
        reasons.append("Older age increases medical risk.")

    if duration >= 5:
        reasons.append("Symptoms have persisted for several days.")

    return reasons