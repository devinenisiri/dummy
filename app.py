from flask import Flask
from flask_restful import Api
from item import Item, Items, Dummy

app = Flask(__name__, template_folder='template')
api = Api(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Dummy, '/dummy')

app.run(port = 5002)





