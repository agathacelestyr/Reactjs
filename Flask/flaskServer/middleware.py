from flaskServer.controller import DbSync
from flask_restful import Resource, Api


class SyncDb(Resource):
    def get(self):
        DbSync().create()