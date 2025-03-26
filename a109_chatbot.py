import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Training data: Example user inputs and corresponding intents
training_data = [
    ("Hello", "greeting"),
    ("Hi", "greeting"),
    ("How are you?", "greeting"),
    ("What's your name?", "name"),
    ("Tell me your name", "name"),
    ("Who are you", "name"),
    ("What can you do?", "capabilities"),
    ("What services do you offer?", "capabilities"),
    ("Bye", "farewell"),
    ("Goodbye", "farewell"),
]

# Split data into inputs (X) and labels (y)
X_train = [pair[0] for pair in training_data]  # User inputs
y_train = [pair[1] for pair in training_data]  # Intents

# Create a pipeline: Convert text to TF-IDF features and apply logistic regression
model = make_pipeline(TfidfVectorizer(), LogisticRegression())

# Train the model
model.fit(X_train, y_train)


def chatbot():
    print("Chatbot is running! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Predict the intent
        predicted_intent = model.predict([user_input])[0]

        # Generate a response based on intent
        responses = {
            "greeting": "Hello! How can I help you?",
            "name": "I'm a simple ML chatbot!",
            "capabilities": "I can answer basic questions based on what I was trained on.",
            "farewell": "Goodbye! Have a nice day!"
        }

        print(f"Chatbot: {responses.get(predicted_intent, 'Sorry, I did not understand that.')}")
        
# Run the chatbot
chatbot()
