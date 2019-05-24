from flask import Flask,jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import json,os,datetime
from flask_cache import Cache
app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
#data base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'aminebenk'

db = SQLAlchemy(app)
#jwt token 
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
#app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)
jwt = JWTManager(app)

@app.before_first_request
def create_tables(): 
    db.create_all()
    
@jwt.needs_fresh_token_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)
api = Api(app)


import views,ressources,models


fileData = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), './populate_db/database.json'), 'r')
data = json.load(fileData)

api.add_resource(ressources.UserRegistration, '/registration')
api.add_resource(ressources.UserLogin,'/login')

api.add_resource(ressources.UserLogoutAccess, '/logout/access')
api.add_resource(ressources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(ressources.TokenRefresh, '/token/refresh')
api.add_resource(ressources.AllUsers,'/users')
api.add_resource(ressources.Chaussures,'/chaussures')
api.add_resource(ressources.ChaussParType,'/chaussures/<string:types>')