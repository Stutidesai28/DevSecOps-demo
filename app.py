from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Intentionally insecure hardcoded secret
API_KEY = "SuperSecretPassword123"

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the DevSecOps Demo!"
    })


@app.route("/hello")
def hello():
    name = request.args.get("name", "World")
    return jsonify({
        "message": f"Hello, {name}"
    })


@app.route("/calc")
def calculate():
    expression = request.args.get("exp", "1+1")

    # Intentionally insecure (SonarQube should detect this)
    result = eval(expression)

    return jsonify({
        "expression": expression,
        "result": result
    })


@app.route("/list")
def list_files():
    directory = request.args.get("dir", ".")

    # Intentionally insecure (Command Injection)
    output = os.popen(f"ls {directory}").read()

    return jsonify({
        "directory": directory,
        "output": output
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)