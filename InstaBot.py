from selenium import webdriver
import BotEngine

chromedriver_path = 'CHROMEDRIVE_PATH_HERE' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

BotEngine.init(webdriver)
BotEngine.update(webdriver)

webdriver.close()
