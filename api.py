from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_data():
    try:
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        FILE_PATH = os.path.join(BASE_DIR, "data.json")

        with open(FILE_PATH) as f:
            return json.load(f)
    except Exception as e:
        print("Error:", e)
        return {}

@app.route("/")
def home():
    return "API Running"

@app.route("/stats")
def stats():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)