from flask import Flask,request,jsonify
from flask_restful import Resource,Api
import nike_data as nd 
import json
app = Flask(__name__)
api = Api(app)
class Chaussures(Resource):
    def get(self):
        chauss = nd.getNikeData('https://store.nike.com/fr/fr_fr/pw/homme-running-chaussures/7puZ8yzZoi3')
        return jsonify(chauss)
api.add_resource(Chaussures,'/')

if __name__ == "__main__":
    app.run(debug = True)