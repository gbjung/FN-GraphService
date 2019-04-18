from environs import Env


env = Env()


NEO4J_HOST = env('NEO4J_HOST', default='localhost')
NEO4J_USER = env('NEO4J_USER', default='neo4j')
NEO4J_PASSWORD = env('NEO4J_PASSWORD', default='0529')
