from flask import request
from flask_restful import Resource
from model.customerTable import Customers
from db import db


class Customer(Resource):
    def put(self):
        print("Reached Request : Executing")
        requestBody = request.json
        newCustomer = Customers(fullName=requestBody.get(
            'name', None), address=requestBody.get('address', None), number=requestBody.get('number', None), prime=requestBody.get('prime', None))
        db.session.add(newCustomer)
        db.session.commit()

    def post(self):
        # TODO : recieve login user request and pass it down to model
        pass


class UpdateUser(Resource):
    def post(self):
        # TODO Update recieved parameters
        pass