from flask import Flask
from flask_cors import CORS

from graph_handler.controllers import graph_routes

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World!"

app.register_blueprint(graph_routes, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)
