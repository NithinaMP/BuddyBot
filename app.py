from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Responses database
RESPONSES = {
    'greetings': [
        "Hello! I'm BuddyBot, here to chat with you!",
        "Hi there! What's on your mind today?",
        "Hey! Great to see you 😊"
    ],
    'how_are_you': [
        "I'm doing great! Thanks for asking 😊",
        "Fantastic as always! How about you?",
        "Pretty good! I'm here and ready to chat 💬"
    ],
    'jokes': [
        "Why don't programmers like nature? Too many bugs! 🐞",
        "Why do Java developers wear glasses? Because they don't C#! 👓",
        "What's a programmer's favorite hangout? The Foo Bar! 🍺",
        "Why did the developer quit? Because they didn't get arrays! 😄"
    ],
    'goodbye': [
        "Goodbye! Have an amazing day 😊",
        "See you later! Take care! 👋",
        "Bye! Come chat anytime 🌟"
    ],
    'fallback': [
        "Hmm, I'm not sure about that. Try asking something else! 🤔",
        "That's interesting! But I don't have an answer yet.",
        "I don't know how to respond to that. Type 'help' to see what I can do!"
    ]
}

def chatbot_response(message):
    """Process user message and return appropriate response."""
    message = message.lower().strip()
    
    # Empty message check
    if not message:
        return "Please type something! I'm here to chat 😊"
    
    # Greetings
    if any(word in message for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice(RESPONSES['greetings'])

    # Identity questions
    elif any(phrase in message for phrase in ["your name", "who are you"]):
        return "I'm BuddyBot, your friendly Flask-powered assistant! 🤖"

    # Status check
    elif any(phrase in message for phrase in ["how are you", "how r u"]):
        return random.choice(RESPONSES['how_are_you'])

    # Jokes
    elif any(word in message for word in ["joke", "funny"]):
        return random.choice(RESPONSES['jokes'])

    # Python related
    elif "python" in message:
        return "Python is an awesome language! Easy to learn and super powerful 🐍"

    # Flask related
    elif "flask" in message:
        return "Flask is a lightweight Python web framework. Perfect for projects like this! 🌐"

    # Help
    elif "help" in message or "what can you do" in message:
        return "I can chat, tell jokes, answer questions about Python/Flask, and more! Just ask away! 💬"

    # Thanks
    elif "thank" in message:
        return "You're welcome! Happy to help 😊"

    # Goodbye
    elif any(word in message for word in ["bye", "goodbye", "see you"]):
        return random.choice(RESPONSES['goodbye'])

    # Default fallback
    else:
        return random.choice(RESPONSES['fallback'])


@app.route("/")
def index():
    """Render the main chat interface."""
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    """Handle POST request to get bot response."""
    try:
        user_message = request.form.get("message", "").strip()
        
        if not user_message:
            return jsonify({"reply": "Please type a message!"}), 400
        
        response = chatbot_response(user_message)
        return jsonify({"reply": response})
    
    except Exception as e:
        return jsonify({"reply": "Sorry, something went wrong! Please try again."}), 500


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template("index.html"), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)