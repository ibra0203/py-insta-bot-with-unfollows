import datetime, TimeHelper
from DBHandler import *
import Constants


def delete_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    sql = "DELETE FROM followed_users WHERE username = '{0}'".format(username)
    cursor.execute(sql)
    mydb.commit()


def add_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(%s,%s)",(username, now))
    mydb.commit()


def add_user_list(users):
    for user in users:
        add_user(user)


def check_user_list():
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    users_to_unfollow = []
    for r in results:
        d = TimeHelper.days_since_date(r[1])
        if d > Constants.DAYS_TO_UNFOLLOW:
            users_to_unfollow.append(r[0])
    return users_to_unfollow


def get_followed_users():
    users = []
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    for r in results:
        users.append(r[0])

    return users


def check_following_user(username):
    cursor = DBHandler.get_mydb().cursor()
    row_count =0
    cursor.execute("SELECT * from followed_users WHERE username = %s", (username,))
    results = cursor.fetchall()
    for r in results:
        return True
    return False