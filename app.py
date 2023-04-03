import json
import os
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError

app = Flask(__name__)
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxx"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt3', methods=['GET', 'POST'])
def gpt3():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages = [user_input]

    try:
        response = openai.Completion.create(
            engine="text-curie-001",
            prompt=messages,
            max_tokens=150   ,
            n=1,
            stop=None,
            temperature=0.7,
        )
        content = response.choices[0].text
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True)
