import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_BEARER_TOKEN = os.getenv("API_BEARER_TOKEN")

if not API_BEARER_TOKEN:
    raise ValueError("API_BEARER_TOKEN is missing in .env")

def verify_token(req):
    auth_header = req.headers.get("Authorization", "")
    return auth_header == f"Bearer {API_BEARER_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API running ✅"})

@app.route("/analyze", methods=["POST"])
def analyze():
    if not verify_token(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    transcript = data.get("text", "")

    if not transcript:
        return jsonify({"error": "Missing text"}), 400

    # Free dummy response
    return jsonify({
        "actions": [
            {
                "task": "Complete backend",
                "owner": "Rahul",
                "deadline": "Thursday"
            },
            {
                "task": "Finish UI",
                "owner": "Priya",
                "deadline": "Friday"
            }
        ],
        "summary": "The team discussed backend and UI tasks with clear deadlines assigned."
    })

if __name__ == "__main__":
    print("Starting server...")
    app.run(host="127.0.0.1", port=5000, debug=True)