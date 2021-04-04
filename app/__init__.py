from flask import Flask
from config import Config
from flask_restful import Api
from app.resources import Film, Films

app = Flask(__name__)

app.config.from_object(Config)

api = Api(app)

api.add_resource(Film, '/film/<string:film_id>')
api.add_resource(Films, '/films')
