from flask import Flask, render_template, request, jsonify, send_from_directory
import json

app = Flask(__name__, static_folder='.', static_url_path='')

with open("chatbot_responses.json") as f:
    responses = json.load(f)

@app.route("/")
def index():
    return app.send_static_file("port.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].lower()
    for keyword, response in responses.items():
        if keyword in user_input:
            return jsonify({"response": response})
    return jsonify({"response": "I'm not sure how to respond to that. Try asking something else!"})

if __name__ == "__main__":
    app.run(debug=True)
