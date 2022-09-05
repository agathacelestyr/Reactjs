from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Store(Resource):
    def get(self, name):
        return{'store-name': name}


api.add_resource