from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes here
    from .routes import hello, add, subtract, mult, divide
    app.add_url_rule('/api/hello', 'hello', hello, methods=['GET'])
    app.add_url_rule('/api/add', 'add', add, methods=['POST'])
    app.add_url_rule('/api/subtract', 'subtract', subtract, methods=['POST'])
    app.add_url_rule('/api/mult', 'mult', mult, methods=['POST'])
    # app.add_url_rule('/api/divide', 'divide', divide, methods=['POST'])

    return app
