from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chatbot(user_input, max_length=50)
    return {'response': response[0]['generated_text']}

if __name__ == '__main__':
    app.run(debug=True)
