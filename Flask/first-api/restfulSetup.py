from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required, JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = 'celesty'
api = Api(app)
CORS(app)

jwt = JWTManager(app)

stores = []


class Item():
    def __init__(self, name, _id, price) -> None:
        self.id = _id
        self.name = name
        self.price = price

    def convertToDict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}


class Store():
    def __init__(self, name: str, _id: int) -> None:
        self.name = name
        self.id = _id
        self.items = []

    def addItem(self, item: Item):
        foundItems = next(filter(lambda x: x.id == item.id), None)
        if foundItems is not None:
            return {'message': 'Item already exists'}
        else:
            self.items.append(item)

    def convertToDict(self):
        # return self.items()
        res = {'name': self.name, 'id': self.id,
               'items': [item.convertToDict() for item in self.items]}
        return {'message': res}


class StoreAPI(Resource):
    def get(self, storeId):
        return {'data': [store.convertToDict() for store in stores]}, 200

    def post(self, storeId):
        try:
            body = request.get_json()
            for i in range(len(stores)):
                if stores[i].id == storeId:
                    stores[i].name = body['name']
                    return {'message': 'Done'}
            return {'message': 'failed'}
        except:
            print("Error Occured ")

    def put(self, storeId):
        body = request.get_json()
        stores.append(Store(body['name'], storeId))
        return {'message': 'Done'}, 201

    def delete(self, storeId):
        for i in range(len(stores)):
            if stores[i].id == storeId:
                stores.pop(i)
                return {'message': 'Done'}
        return {'message': 'failed'}


class UserAuth(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        # TODO : authenticate User
        token = create_access_token(
            identity={'username': username})
        return {"token": token}

    @jwt_required()
    def put(self):
        username = get_jwt_identity()
        return {"message": username}


# * now make an Api for geting an item from a store

def getItem(self):
    res = {'name': self.name, 'id': self.id,
           'items': [item.getItem() for item in self.items]}
    return {'message': res}


class ItemAPI(Resource):
    def get(self, storeId, ItemId):
        res = next(filter(lambda x: x.id == storeId, stores), None)
        if res is None:
            return {"message": "Store not found"}
        else:
            for item in res.items:
                if item.id == ItemId:
                    return item.getItem()
            return {'message': 'Items not found'}

# * put a new item to a store

class Store():
    def addItem(self, item: Item):
        foundItems = next(filter(lambda x: x.id == item.id), None)
        if foundItems is None:
            return {'message': 'Item already exists'}
        else:
            self.items.append(item)

# * modify price of an item in the store

def post(self, storeId, ItemId):
    try:
        body = request.get_json()
        for i in range(len(stores)):
            if stores[i].id == storeId:
                stores[i].name = body['name']
                return {'message': 'Done'}
        return {'message': 'failed'}
    except:
        print("Error Occured ")
# * remove an item from the store

def delete(self, storeId, ItemId):
    for i in range(len(stores)):
        if stores[i].id == storeId:
            stores.pop(i)
            return {'message': 'Done'}
    return {'message': 'failed'}


api.add_resource(StoreAPI, '/store/<int:storeId>')
api.add_resource(UserAuth, '/user')


app.run(debug=True, port=5000)