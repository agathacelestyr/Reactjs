from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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
        res = {'name': self.name, 'id': self.id, 'items': (
            item.convertToDict() for item in self.items)}
        return{'message': res}


class StoreAPI(Resource):
    def get(self, storeId):
        res = next(filter(lambda x: x.id == storeId, stores), None)
        return res.convertToDict() if res is not None else {'message': 'Not found'}

    def post(self, storeId):
        try:
            body = request.get_json()
            for i in range(len(stores)):
                if stores[i].id == storeId:
                    stores[i].name = body['name']
                    return {'message', 'Done'}
            return {'message': 'failed'}
        except:
            print("Error Occured")

    def put(self, storeId):
        body = request.get_json()
        stores.append(Store(body['name'], storeId))
        return {'message': 'Done'}

    def delete(self, storeId):
        for i in range(len(stores)):
            if stores[i].id == storeId:
                stores.pop(i)
                return {'message': 'Done'}
        return {'message': 'failed'}


api.add_resource(StoreAPI, '/store/<int:storeId>')


app.run(debug=True, port=5000)
