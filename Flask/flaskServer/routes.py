from distutils.log import debug
from flask import Flask
from flaskServer.middleware import SyncDb
from flask_restful import Api

app = Flask(__name__)
app = Api(app)

# ! initialize DB
app.add_resource(SyncDb, '/db')

app.run(debug=True, port=5000)