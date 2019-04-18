import settings
from py2neo import Graph

from flask import Flask, jsonify, request
from models import Person

app = Flask(__name__)

graph = Graph(
    host=settings.NEO4J_HOST,
    port=settings.NEO4J_PORT,
    user=settings.NEO4J_USER,
    password=settings.NEO4J_PASSWORD,
)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/people')
def get_people():
    people = [person for person in Person.match(graph)]
    print(people)
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True)
