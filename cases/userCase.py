from data import mysq_m
from cases.util.resultWrapper import xSuccess, xFail

USERS_TABLE = 'all_users_table'
USER_TABLE_TUPLE = (USERS_TABLE,)
USER_OWN_MESSAGE_TABLE = "own_user_table"

mysq_m.USERS_TABLE = USERS_TABLE
mysq_m.USER_TABLE_TUPLE = USER_TABLE_TUPLE

class User():
    def __init__(self, fullLogin, login, password, uniqueId, about):
        self.fullLogin = ""
        self.login = ""
        self.password = ""
        self.uniqueId = ""
        self.about = ""

    def map(self, list: list):
        self.fullLogin = list[0]
        self.login = list[1]
        self.password = list[2]
        self.uniqueId = list[3]
        self.about = list[4]

def checkUserTable():
    result = mysq_m.isTableExists(USER_TABLE_TUPLE)
    if not result:
        mysq_m.createUsersTable(USER_TABLE_TUPLE)


def getUser(uniqueName: str):
    row = mysq_m.getUser(uniqueName)
    if len(row) == 0:
        result = xFail()
        result["details"] = "No user with fullLogin" + uniqueName + "found"
        return result, 404
    r = xSuccess()
    r["details"] = User(
        fullLogin=row[0],
        login=row[1],
        password=row[2],
        uniqueId=row[3],
        about=row[4]
    )
    return r, 200


#    API call   #
def create_user(user: User):
    row = mysq_m.getUser(user.fullLogin)
    if len(row) != 0:
        r = xFail(r_details="User " + user.fullLogin + " already exists")
        return r, 422
    else:
        return createUser(user)


def createUser(user:User):
    userTuple = mysq_m.addUser(
        (user.fullLogin,
         user.login,
         user.about,
         user.uniqueId,
         user.password,)
    )
    user_id = mysq_m.addUser(userTuple)
    if user_id == -1:
        return xFail(
            r_details="DataBase Error when add user with fullLogin: " + user.fullLogin
        )
    else:
        rs = mysq_m.create_user_message_table(user.fullLogin)
        if rs:
            return xSuccess()
        else:
            return xFail(
                r_details="DataBase Error when create message table for user with fullLogin: " + user.fullLogin
            )


