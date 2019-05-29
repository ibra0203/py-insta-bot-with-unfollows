# py-insta-bot-with-unfollows
[Tutorial/Explanation article](https://medium.com/@modyari/building-an-instagram-bot-in-python-and-selenium-to-gain-more-followers-4c465f1a2ab5)
## An Instagram bot written in Python that does the following: 
* Browsing specified hashtags and liking random posts 
* Following posters of these posts
* Keeping track of followed users and unfollowing them after a specified number of days
* Allows for customization of settings through a single .json file

## Requirements 
The following libraries are required for the bot to work:
* PyHamcrest
* mysql-connector 
* selenium

The bot needs to connect to a database to store and query the users.
The database name can be changed from settings.json.

The bot requires one table called followed_users within the database with two fields (username, date_added)

## Installation
1. Fill in the missing information in settings.json
2. Change line 4 in InstaBot.py to include your chromedrive path
3. run InstaBot.py:
```
python InstaBot.py
```



## Settings 
```
"config": {
    "days_to_unfollow": 1,
    "likes_over": 150,
    "check_followers_every": 3600,
    "hashtags": []
  }
```

**days_to_unfollow:** number of days before unfollowing users

**likes_over:** ignore posts if the number of likes is above this number

**check_followers_every:** number of seconds before checking if it's time to unfollow any of the users

**hashtags:** a list of strings with the hashtag names the bot should be active on
