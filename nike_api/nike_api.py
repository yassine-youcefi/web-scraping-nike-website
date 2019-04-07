from flask import Flask,request,jsonify,make_response
from flask_restful import Resource,Api
import threading
import nike_data as nd 
import json

app = Flask(__name__)
api = Api(app)


class Homepage(Resource):
    def get(self):
        return app.send_static_file('homepage.html')

class Produits(Resource):
    def get(self,produit,types = None):
        if types == None:
            try:
                
                return nd.getNikeData('https://store.nike.com/fr/fr_fr/pw/homme-chaussures/7puZoi3')
            except:
                return make_response(jsonify({'status':404,'msg': 'Not found'}), 404)
        else:
            try:
                return jsonify(nd.getNikeData(urls[types][produit]))
            except:
                return make_response(jsonify({'status':404,'msg': 'Not found'}), 404)


api.add_resource(Homepage,'/')
api.add_resource(Produits,'/<string:produit>','/<string:produit>/<string:types>')


if __name__ == "__main__":
    app.run(debug = True)