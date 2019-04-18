import os

IS_PROD = os.environ.get('HEROKU', None)

if IS_PROD:
    NEO4J_HOST = os.environ.get('NEO4J_HOST', None)
    NEO4J_USER = os.environ.get('NEO4J_USER', None)
    NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')
else:
    from environs import Env
    env = Env()
    NEO4J_HOST = env('NEO4J_HOST', default='localhost')
    NEO4J_USER = env('NEO4J_USER', default='neo4j')
    NEO4J_PASSWORD = env('NEO4J_PASSWORD', default='0529')
