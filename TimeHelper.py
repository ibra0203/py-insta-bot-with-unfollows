import datetime


def days_since_date(n):
    diff = datetime.datetime.now().date() - n
    return diff.days