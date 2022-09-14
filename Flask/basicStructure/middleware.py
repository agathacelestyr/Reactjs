from controller import DbSync
from controller import CustomersCont
from flask_restful import Resource, Api
from flask import request


class SyncDb(Resource):
    def get(self):
        DbSync().create()


class Customers(Resource):

    def put(self):
        reqObj = request.json
        name, address, number, prime = reqObj["name"], reqObj["address"], reqObj["number"], reqObj["prime"]
        customer = CustomersCont().addCloth(name, address, number, prime)
        print(customer)