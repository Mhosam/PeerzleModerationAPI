from flask import Flask, jsonify, request
import os
import openai

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Retrieve the input from the request JSON body
    data = request.get_json()
    user_input = data.get('input', '')

    response = openai.Moderation.create(
        input=user_input
    )

    output = response["results"][0]

    return jsonify(output), 200

if __name__ == '__main__':
    app.run(debug=True)
