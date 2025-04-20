from flask import Flask, request, jsonify
import random
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def get_bot_response(user_message):
    user_message = user_message.lower()

    responses = {
        "hello": ["Hi there!", "Hello! How can I assist you today?", "Hey! How's it going?"],
        "how are you": ["I'm doing well, thanks for asking!", "I'm great, how about you?", "I'm doing great, how can I help you today?"],
        "bye": ["Goodbye! Take care!", "See you later!", "Goodbye, have a great day!"],
        "name": ["I'm a chatbot, I don't have a name!", "I don't have a name, but you can call me chatbot.", "I'm just your friendly chatbot!"],
        "joke": ["Why don't skeletons fight each other? They don't have the guts!", "I told my computer I needed a break... It froze!", "Why did the math book look sad? Because it had too many problems!"]
    }

    for key, values in responses.items():
        if re.search(r"\b" + re.escape(key) + r"\b", user_message):
            return random.choice(values)

    return "Hmm, I didn't quite catch that. Could you try again?"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
