from backend.predictor import predict
from backend.recommendation import get_recommendation
from backend.chatbot import chatbot_response

# Sample patient data
prediction = predict(
    age=65,
    temperature=39.5,
    heart_rate=120,
    pain_level=9,
    symptom="Chest Pain",
    duration=3
)

print("===== Prediction =====")
print(prediction)

recommendation = get_recommendation(prediction)

print("\n===== Recommendation =====")
print(recommendation)

print("\n===== Chatbot =====")
print(chatbot_response("What should I do?", prediction))

print("\n===== Greeting =====")
print(chatbot_response("Hello"))

print("\n===== Fever Question =====")
print(chatbot_response("I have a fever"))