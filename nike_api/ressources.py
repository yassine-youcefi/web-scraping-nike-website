from flask_restful import Resource,reqparse
from models import UserModel,RevokedTokenModel
from flask_jwt_extended import (create_access_token,create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask import jsonify,request
import run,json,os

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)



class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'. format(data['username'])}
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])

            return {
                'code':201,
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token
                }
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500



class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()
    
    def delete(self):
        return UserModel.delete_all()


#nike classes

class Chaussures(Resource):
    @jwt_required
    @run.cache.cached(timeout=5)
    def post(self):
        return {"code":200,"msg":"found","data":[run.data[0]]}

class ChaussParType(Resource):
    @jwt_required
    @run.cache.cached(timeout=5)
    def post(self,types):
        category = request.args.get('category')
        minPrice = request.args.get('minPrice')
        maxPrice = request.args.get('maxPrice')
        productName = request.args.get('productName')
        price = request.args.get('price')
        
        try:
            data = run.data[0][types][0]["chaussures"]
            if productName:
                data = [p for p in data if productName.lower() in p['productName'].lower()]
            if category:
                data = [p for p in data if p['category'] == category]
            if minPrice:
                data = [p for p in data if float(p['price'].replace(',','.').split(' ')[0]) >= float(minPrice)]
            if maxPrice:
                data = [p for p in data if float(p['price'].replace(',','.').split(' ')[0]) <= float(maxPrice)]
            if price and maxPrice == None and minPrice == None:
                data = [p for p in data if float(p['price'].replace(',','.').split(' ')[0]) == float(price)]
            elif price != None:
                return {"code":400,"msg":"Bad Request"}
            return {"code":200,"msg":"found","data":data}
            
        except KeyError:
            return {"code":400,"msg":"Bad Request"}
        