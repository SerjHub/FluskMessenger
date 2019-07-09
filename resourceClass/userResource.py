from flask_restful import Resource, reqparse
import cases.userCase as userCase
from cases.userCase import User

class UserResource(Resource):
    def get(self, name):
        userResult = userCase.getUser(name)
        return userResult[0], userResult[1]   #

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("fullLogin")
        parser.add_argument("login")
        parser.add_argument("password")
        parser.add_argument("uniqueId")
        parser.add_argument("about")
        args = parser.parse_args()
        postUser = User(
            fullLogin=args["fullLogin"],
            login=args["login"],
            password=args["password"],
            uniqueId=args["uniqueId"],
            about=args["about"]
        )
        postResult = userCase.create_user(postUser)
        return postResult[0], postResult[1]
