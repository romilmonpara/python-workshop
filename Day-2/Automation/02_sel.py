from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

print("Page Title: ", driver.title)
time.sleep(3)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("What Is Selenium in Python?")
search_box.send_keys(Keys.ENTER)

time.sleep(7)
driver.quit()