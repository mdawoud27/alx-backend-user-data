#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def index() -> str:
    """Home page"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
