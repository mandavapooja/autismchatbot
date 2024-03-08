import logging
from flask import Flask, render_template, request
from chatbot import chatbot_response

app = Flask(__name__, template_folder='template')

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    logging.debug("User Input: %s", user_input)  # Log the user input
    response = chatbot_response(user_input)
    logging.debug("Chatbot Response: %s", response)  # Log the chatbot response
    
    # Error handling: Check if the response is empty
    if not response:
        response = "Oops! Something went wrong. Please try again later."
        logging.error("Empty response from chatbot.")

    return response

if __name__ == '__main__':
    app.run(debug=True)
