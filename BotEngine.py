import AccountAgent, DBUsers
import Constants
import datetime


def init(webdriver):
    Constants.init()
    AccountAgent.login(webdriver)


def update(webdriver):
    start = datetime.datetime.now()
    _check_follow_list(webdriver)
    while True:
        AccountAgent.follow_people(webdriver)
        end = datetime.datetime.now()
        elapsed = end - start
        if elapsed.total_seconds() >= Constants.CHECK_FOLLOWERS_EVERY:
            start = datetime.datetime.now()
            _check_follow_list(webdriver)


def _check_follow_list(webdriver):
    print("Checking for users to unfollow")
    users = DBUsers.check_user_list()
    if len(users) > 0:
        AccountAgent.unfollow_people(webdriver, users)