import mysql.connector
import Constants
class DBHandler:
    def __init__(self):
        DBHandler.HOST = Constants.HOST
        DBHandler.USER = Constants.USER
        DBHandler.DBNAME = Constants.DATABASE
        DBHandler.PASSWORD = Constants.PASS
    HOST = Constants.HOST
    USER = Constants.USER
    DBNAME = Constants.DATABASE
    PASSWORD = Constants.PASS
    @staticmethod
    def get_mydb():
        if DBHandler.DBNAME == '':
            Constants.init()
        db = DBHandler()
        mydb = db.connect()
        return mydb

    def connect(self):
        mydb = mysql.connector.connect(
            host=DBHandler.HOST,
            user=DBHandler.USER,
            passwd=DBHandler.PASSWORD,
            database = DBHandler.DBNAME
        )
        return mydb



