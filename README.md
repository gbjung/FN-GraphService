# FN-GraphService
Exploratory graph project for the FiscalNote Hackathon


SETUP:
1. pip install -r requirements.txt

2. create a .env file in the top directory level with these filled in
NEO4J_HOST=localhost:24780
NEO4J_USER=admin
NEO4J_PASSWORD=somepassword


RUN:
python app.py

INSTRUCTIONS:
Adding nodes:
POST json to /nodes

Adding edges:
POST json to /edges

Check graph_handler/dummy_data.py for node/edge structure
