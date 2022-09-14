from flask import request
from flask_restful import Resource


class Customer(Resource):
    def put(self):
        # TODO : recieve creat user request and pass it down to model
        pass

    def post(self):
        # TODO : recieve login user request and pass it down to model
        pass


class UpdateUser(Resource):
    def post(self):
        # TODO Update recieved parameters
        pass