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
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400
    
    return jsonify({"result": num1 + num2})

@app.route("/api/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    try:
        num1 = int(data['num1'])
        num2 = int(data['num2'])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400
    
    return jsonify({"result": num1 - num2})


@app.route("/api/mult", methods=["POST"])
def mult():
    data = request.get_json()
    try:
        num1 = int(data['num1'])
        num2 = int(data['num2'])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400
    
    return jsonify({"result": num1 * num2})


# Use before_request instead of before_first_request
@app.before_request
def before_request():
    print("This will run before every request.")

if __name__ == "__main__":
    app.run(debug=True)
