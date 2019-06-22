from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name" : "Xach",
        "age"  : 42
    },
    {
        "name" : "pidor",
        "age"  : 13
    }
]

class User(Resource):
    def get(selfm ,name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return  "User not found", 404


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        args = parser.parse_args()
        for user in users:
            if name == user["name"]:
                return "User with name {} already exists".format(name)

        user = {
            "name" : name,
            "age"  : args["age"]
        }
        users.append(user)
        return user, 201

api.add_resource(User, "/user/<string:name>")
app.run(debug=True,port=8000)

