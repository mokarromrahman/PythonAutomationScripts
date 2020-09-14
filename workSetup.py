import time
from selenium import webdriver  # need for automation
# use these to read the .env file
import dotenv
import os

PATH = "D:\Desktop\chromedriver_win32\chromedriver.exe"  # path of chrome web driver
# tell the driver that this is where it is location and to use chrome
driver = webdriver.Chrome(PATH)

driver.get("https://apps.ualberta.ca/")
time.sleep(1)
driver.find_element_by_xpath(
    "/html/body/div[2]/div/div[1]/div[1]/div[1]/div[1]/a").click()
time.sleep(1)
print(os.getenv('UALBERTA_EMAIL'))
# driver.find_element_by_id("username").send_keys(os.getenv('UALBERTA_EMAIL'))
