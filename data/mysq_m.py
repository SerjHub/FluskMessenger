import mysql.connector as mysql
from config import mysql_pass

USERS_TABLE = ""
USER_TABLE_TUPLE = ""
USER_MESSAGE_TABLE = ""

db = mysql.connect(
    host="localhost",
    user="root",
    passwd=mysql_pass,
    database="MagicMessenger",
    auth_plugin='mysql_native_password'
)
print()

cursor = db.cursor()


def isTableExists(table_name):
    cursor.execute("show tables")
    tables = cursor.fetchall()
    return tables.count(table_name) > 0


def createUsersTable():
    cursor.execute(
        "CREATE TABLE "
        + USERS_TABLE
        + " (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
          " fullLogin VARCHAR(255),"
          " login VARCHAR(255),"
          " password VARCHAR(255),"
          " about VARCHAR(255),"
          " uniqueId VARCHAR(255))")


# unique: fullLogin, uniqueId
def addUser(user: tuple):
    query = 'INSERT INTO ' \
            + USERS_TABLE \
            + ' (fullLogin, login, password, about, uniqueId) VALUES(%s, %s, %s, %s, %s)'
    values = (
        user[0],
        user[1],
        user[2],
        user[3],
        user[4])
    cursor.execute(query, values)
    db.commit()
    rc = cursor.rowcount
    return cursor.lastrowid if rc != -1 else -1


def getUser(login: str):
    query = "SELECT * FROM " + USERS_TABLE + " WHERE fullLogin = %s"
    cursor.execute(query, (login,))
    return cursor.fetchall()


def create_user_message_table(userId):
    cursor.execute(
        "CREATE TABLE "
        + USER_MESSAGE_TABLE + userId
        + " (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
          " text VARCHAR(255),"
          " friendFullLogin VARCHAR(255),"
          " datetime DATETIME)"
    )
    cursor.execute("show tables")
    tables = cursor.fetchall()
    return tables.count((USER_MESSAGE_TABLE + userId,)) > 0
