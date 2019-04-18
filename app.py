import settings
from py2neo import Graph, authenticate

from flask import Flask, jsonify
from models import Person
from serializer import PersonSerializer

app = Flask(__name__)

authenticate(settings.NEO4J_HOST, settings.NEO4J_USER, settings.NEO4J_PASSWORD)
graph = Graph("https://{}".format(settings.NEO4J_HOST),
              bolt=False)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/people')
def get_people():
    people = [PersonSerializer(person) for person in Person.select(graph)]
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True)
