from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Serveur Dashboard L14 fonctionne"
    })


@app.route("/api/test")
def test():
    return jsonify({
        "status": "ok",
        "message": "API Dashboard L14 fonctionne"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
