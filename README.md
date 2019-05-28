# insta-bot-with-unfollows

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

The bot needs to connect to a database to store and query the users 
The database name can be changed from settings.json 

The bot requires one table called followed_users within the database with two fields (username, date_added)

## Installation
After filling in the missing information in settings.json, run InstaBot.py 
```
python InstaBot.py
```
