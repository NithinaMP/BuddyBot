from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()
    
    # Greetings
    if "hello" in message or "hi" in message or "hey" in message:
        responses = [
            "Hello! I'm BuddyBot, here to chat with you!",
            "Hi there! What's on your mind today?",
            "Hey! Great to see you 😊"
        ]
        return random.choice(responses)
    
    # Name
    elif "your name" in message or "who are you" in message:
        return "I'm BuddyBot, your friendly Flask-powered assistant! 🤖"
    
    # How are you
    elif "how are you" in message or "how r u" in message:
        responses = [
            "I'm doing great! Thanks for asking!",
            "Fantastic as always! How about you?",
            "Pretty good! I'm here and ready to chat!"
        ]
        return random.choice(responses)
    
    # Jokes
    elif "joke" in message or "funny" in message:
        jokes = [
            "Why don't programmers like nature? Too many bugs! 🐞",
            "Why do Java developers wear glasses? Because they don't C#! 👓",
            "What's a programmer's favorite place? The Foo Bar! 🍺",
            "Why did the developer quit? Because they didn't get arrays! 😄"
        ]
        return random.choice(jokes)
    
    # Python
    elif "python" in message:
        return "Python is an awesome language! Easy to learn and super powerful 🐍"
    
    # Flask
    elif "flask" in message:
        return "Flask is a lightweight Python web framework. Perfect for projects like this! 🌐"
    
    # Help
    elif "help" in message:
        return "I can chat, tell jokes, answer questions about Python/Flask, and more! Just ask!"
    
    # Thanks
    elif "thank" in message:
        return "You're welcome! Happy to help 😊"
    
    # Bye
    elif "bye" in message or "goodbye" in message or "see you" in message:
        responses = [
            "Goodbye! Have an amazing day 😊",
            "See you later! Take care! 👋",
            "Bye! Come chat anytime 🌟"
        ]
        return random.choice(responses)
    
    # Default
    else:
        return "Hmm, I'm not sure about that. Try asking something else! 🤔"

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