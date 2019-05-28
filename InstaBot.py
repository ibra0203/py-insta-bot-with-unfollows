from selenium import webdriver
import BotEngine

chromedriver_path = 'D:/chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

BotEngine.init(webdriver)
BotEngine.update(webdriver)

webdriver.close()
