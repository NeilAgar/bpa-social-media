from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.home import HomePage

load_dotenv(".env", verbose=True)

app = Flask(__name__)
app.config.from_pyfile('config.py')

api = Api(app)
jwt = JWTManager(app)

api.add_resource(HomePage, "/")

if __name__ == "__main__":
    app.run()
