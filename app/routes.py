from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    try:
        num1 = int(data['num1'])
        num2 = int(data['num2'])
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"}), 400
    
    return jsonify({"result": num1 + num2})

@app.route("/api/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    try:
        # Use 'minuend' and 'subtrahend' instead of 'num1' and 'num2'
        num1 = int(data['minuend'])
        num2 = int(data['subtrahend'])
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"}), 400
    
    return jsonify({"result": num1 - num2})


@app.route("/api/mult", methods=["POST"])
def mult():
    data = request.get_json()
    try:
        num1 = int(data['num1'])
        num2 = int(data['num2'])
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"}), 400
    
    return jsonify({"result": num1 * num2})

@app.route("/api/divide", methods=["POST"])
def divide():
    data = request.get_json()
    try:
        numerator = int(data['numerator'])
        denominator = int(data['denominator'])
        if denominator == 0:
            return jsonify({"error": "Division by zero"}), 400
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"}), 400

    return jsonify({"result": numerator / denominator})


@app.before_request
def before_request():
    # You can use this to log or perform actions before each request
    print("This will run before every request.")

if __name__ == "__main__":
    app.run(debug=True)
