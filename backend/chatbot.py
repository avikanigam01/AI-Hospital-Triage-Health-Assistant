import random

responses = {

    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening", "hii"],
        "responses": [
            "Hello! 👋 I'm your AI Health Assistant. How are you feeling today?",
            "Hi there! 😊 Tell me what's bothering you today.",
            "Welcome! I'm here to help with your health-related questions. How can I assist you?"
        ]
    },
    "about": {
    "keywords": [
        "who are you",
        "what are you",
        "your name",
        "introduce yourself"
    ],
    "responses": [
        "I'm an AI Health Assistant designed to provide preliminary health guidance, explain common symptoms, and help you understand your triage assessment. I'm not a substitute for a qualified healthcare professional."
    ]
    },

    "fever": {
        "keywords": ["fever", "temperature", "hot"],
        "responses": [
            "🤒 A fever is often a sign that your body is fighting an infection. Stay hydrated and rest.",
            "Monitor your temperature regularly. If it goes above 39°C or lasts more than 2–3 days, consult a doctor.",
            "Drink plenty of fluids and avoid dehydration."
        ]
    },

    "headache": {
        "keywords": ["headache", "head pain", "migraine"],
        "responses": [
            "A headache can be caused by stress, dehydration, or lack of sleep. Try resting and drinking water.",
            "If your headache is severe, sudden, or accompanied by vision changes or weakness, seek medical care immediately."
        ]
    },

    "cough": {
        "keywords": ["cough"],
        "responses": [
            "A cough can have many causes, including viral infections or allergies. Stay hydrated and monitor your symptoms.",
            "If your cough lasts more than two weeks or is accompanied by difficulty breathing, consult a doctor."
        ]
    },

    "dehydration": {
        "keywords": ["dehydration", "dehydrated"],
        "responses": [
            "Drink water or ORS in small, frequent sips. Dark urine and dizziness may be signs of dehydration.",
            "If you are unable to keep fluids down or feel faint, seek medical attention."
        ]
    },
    "help": {
    "keywords": ["help", "what can you do", "how can you help"],
    "responses": [
        "I can:\n\n• Explain common symptoms\n• Provide basic first-aid guidance\n• Help you understand your AI triage result\n• Answer general health questions\n\nPlease remember that I do not replace a qualified healthcare professional."
    ]
    },

    "emergency": {
        "keywords": ["emergency", "chest pain", "can't breathe", "difficulty breathing", "bleeding"],
        "responses": [
            "⚠️ Your symptoms may require urgent medical attention. Please visit the nearest emergency department immediately.",
            "If you have severe chest pain, trouble breathing, or heavy bleeding, call emergency services right away."
        ]
    },

    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "responses": [
            "You're welcome! 😊 Take care and stay healthy.",
            "Happy to help! If you have any more questions, feel free to ask."
        ]
    },

    "bye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": [
            "Goodbye! 👋 Take care of yourself.",
            "Stay healthy! Feel free to come back anytime."
        ]
    }

}


def chatbot_response(message, prediction=None):

    if prediction:

        risk = prediction.get("risk")
        department = prediction.get("department")

        advice_questions = [
            "what should i do",
            "what now",
            "what next",
            "should i go to hospital",
            "do i need a doctor",
            "is it serious",
            "can i wait"
        ]

        if any(question in message for question in advice_questions):
            # Return advice based on prediction

            if risk == "Emergency":
                return (
                    f"Based on the information you submitted, your condition has been classified as "
                    f"**{risk}**.\n\n"
                    f"I recommend visiting the **{department}** immediately.\n\n"
                    f"If your symptoms worsen or you experience severe difficulty breathing, chest pain, "
                    f"or loss of consciousness, seek emergency medical care without delay."
                )

            elif risk == "Urgent":
                return (
                    f"Your symptoms appear {risk}. "
                    f"Please visit the {department} as soon as possible."
                )

            else:
                return (
                    f"Your condition appears {risk}. "
                    f"You should still consult {department} if symptoms worsen."
                )
    message = message.lower().strip()

    for intent in responses.values():
        for keyword in intent["keywords"]:
            if keyword in message:
                return random.choice(intent["responses"])

    return (
        "I'm sorry, I didn't quite understand that. 😊 "
        "You can ask me about fever, headache, cough, dehydration, emergency symptoms, "
        "or tell me how you're feeling."
    )