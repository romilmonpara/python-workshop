from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

print("Page Title: ", driver.title)
time.sleep(3)

driver.quit()