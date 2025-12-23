from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()
    
    # Greetings
    if "hello" in message or "hi" in message or "hey" in message:
        responses = [
            "Hello! How can I help you?",
            "Hi there! What's up?",
            "Hey! Nice to meet you!"
        ]
        return random.choice(responses)
    
    # Name
    elif "your name" in message or "who are you" in message:
        return "I'm a chatbot built with Flask!"
    
    # How are you
    elif "how are you" in message:
        responses = [
            "I'm doing great! Thanks for asking!",
            "I'm good! How about you?",
            "Pretty good! Just chatting away!"
        ]
        return random.choice(responses)
    
    # Jokes
    elif "joke" in message or "funny" in message:
        jokes = [
            "Why don't programmers like nature? Too many bugs! 🐞",
            "Why do Java developers wear glasses? Because they don't C#! 👓",
            "What's a programmer's favorite place? The Foo Bar! 🍺"
        ]
        return random.choice(jokes)
    
    # Python
    elif "python" in message:
        return "Python is an amazing programming language! 🐍"
    
    # Flask
    elif "flask" in message:
        return "Flask is a lightweight Python web framework! 🌐"
    
    # Bye
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day! 👋"
    
    # Default
    else:
        return "Sorry, I didn't understand that. Try asking something else!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["message"]
    response = chatbot_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)