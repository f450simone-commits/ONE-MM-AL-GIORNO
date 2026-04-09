from flask import Flask, render_template, jsonify
from frase_engine import genera_frase

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/frase")
def frase():
    return jsonify({"frase": genera_frase()})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)