from flask import Flask
from config import config
from resourceClass.userResource import  UserResource
from cases.userCase import checkUserTable
#from data.mysq_m import USERS_TABLE
from flask_restful import Api
#from data.sqlWorker import  get_user_table

Config = config
msqlQ = Config

app = Flask(__name__)
api = Api(app)

#api.add_resource(UserResource, "/user/<string:name>")
api.add_resource(UserResource, "/user")
path = "/user/login/"#key=fullLogin,key=password



checkUserTable()


app.run(debug=True,port=8000,host='0.0.0.0')

