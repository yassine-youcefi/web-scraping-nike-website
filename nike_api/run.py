from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from flask_cache import Cache
app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'aminebenk'
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

api = Api(app)

import views,ressources,models

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(ressources.UserRegistration, '/registration')
api.add_resource(ressources.UserLogin,'/login')
api.add_resource(ressources.AllUsers,'/users')
api.add_resource(ressources.Chaussures,'/chaussures')