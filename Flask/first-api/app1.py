from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/")
def initiate():
    reqObj = request.get_json()
    print(f"Name is {reqObj['name']} and id {reqObj['id']}")
    reqObj["id"] = 45
    return jsonify(reqObj)


stores = [{"name": "Angel Store", "items": [
    {"name": "Shirt", "qty": 56},
    {"name": "Pants", "qty": 34}
]
}]


@app.route("/stores")
def getAllStores():
    return jsonify({"data": stores})


@app.route("/store/items", methods=["POST"])
def getAllItemsOfStore():
    requestObj = request.get_json()
    for store in stores:
        if store["name"] == storeId["id"]:
            return jsonify({"data": store["items"]})
    return jsonify({"data": []})


@app.route("/store/item/qt", methods=["POST"])
def getAllItemsOfStore():
    requestObj = request.get_json()
    for store in stores:
        if store["name"] == requestObj["storeId"]:
            for item in store["items"]:
                if item["name"] == requestObj["itemId"]:
                    return jsonify({"data": item["qty"]})
            return jsonify({"data": []})


@app.route("/add/store")
def getAllStores():
    newStore = request.get_json()
    stores.append(newStore)
    return jsonify({"data": stores})


@app.route("/add/item")
def getAllStores():
    reqObj = request.get_json()
    for i in range(len(stores)):
        if stores[i] == reqObj["storeId"]:
            stores[i]["items"].append(reqObj)


app.run(debug=True, port=5000)


@app.route("/changing/<int:storeId>/<int:itemid>/item", methods=["POST"])
def getChangingitem(storeId, itemId):
    reqObj = request.get_json()
    for store in stores:
        if store["id"] == storeId:
            for storeitem in store["items"]:
                if storeitem["id"] == itemId:
                    storeitem["qty"] = reqObj['qty']
                    print(stores)

                else:
                    print("PRODUCT NOT FOUND")

        else:
            print("STORE NOT FOUND")

    return "request complete"
