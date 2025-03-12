from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login")
time.sleep(5)
username=driver.find_element(By.NAME,"username")
password=driver.find_element(By.NAME,"password")

username.send_keys("---Dummy Instagram Account Id---")
password.send_keys("-----Password-----")

password.send_keys(Keys.ENTER)
time.sleep(5)

driver.get("https://www.instagram.com/explore/tags/mountain")
time.sleep(7)
posturl="https://www.instagram.com/p/C73GMuNvF2s/"

driver.get(posturl)
time.sleep(5)

pyautogui.moveTo(829,810,3)
pyautogui.click()

input("enter to close")
driver.quit()
