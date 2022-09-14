from flask import Flask
from routes.index import addRoutes

app = Flask(__name__)
# TODO : Define your secret key here
# ? app.config["JWT_SECRET_KEY"] = "some-random-text"
addRoutes(app)

app.run(debug=True, port=5000)