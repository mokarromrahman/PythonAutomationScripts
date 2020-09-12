# selenium test
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver  # need for automation
import time
PATH = "D:\Desktop\chromedriver_win32\chromedriver.exe"  # path of chrome web driver
# tell the driver that this is where it is location and to use chrome
driver = webdriver.Chrome(PATH)

driver.get("https://mokarrom.com")
print("title is: " + driver.title)
time.sleep(5)
driver.close()
