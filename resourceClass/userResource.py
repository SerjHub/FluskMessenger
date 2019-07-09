from flask_restful import Resource, reqparse
import cases.userCase as userCase
from cases.userCase import User

users = [
    {
        "name": "Xach",
        "age": 42
    },
    {
        "name": "pidor",
        "age": 13
    }
]


class UserResource(Resource):
    def get(self, name):
        userResult = userCase.getUser(name)
        return userResult[0], userResult[1]   #

    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        ll = fullLogin=args["fullLogin"]
        postUser = User(
            fullLogin=args["fullLogin"],
            login=args["login"],
            password=args["password"],
            uniqueId=args["uniqueId"],
            about=args["about"]
        )
        postResult = userCase.create_user(postUser)
        return postResult[0], postResult[1]
