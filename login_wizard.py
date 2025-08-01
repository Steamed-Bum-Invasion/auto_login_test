from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()

browser = webdriver.Chrome(options=options)

# Visit the specified webpage
url = "https://practicetestautomation.com/practice-test-login/"
browser.get(url)

# Input the username and password
browser.find_element(By.NAME, "username").send_keys("student")
browser.find_element(By.NAME, "password").send_keys("Password123")

# Click the "Log in" button
browser.find_element(By.NAME, "login").click()

# Wait for a while to observe the result (instead of an infinite loop)
time.sleep(30)

# Optional: close the browser after 30 seconds
browser.quit()
