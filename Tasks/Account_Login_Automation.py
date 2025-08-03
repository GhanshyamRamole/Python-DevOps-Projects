from selenium import webdriver
import requests


# login to socal media 

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

email_field = driver.find_element_by_id("email")
email_field.send_keys("7385152019")

password_field = driver.find_element_by_id("pass")
password_field.send_keys("DarkCloud@23")

login_button = driver.find_element_by_id("loginbutton")
login_button.click()


# login to git hub

import requests

username = "your_username"
token = "your_personal_access_token"

response = requests.get("https://api.github.com/user", auth=(username, token))

if response.status_code == 200:
    print("Login successful:", response.json())
else:
    print("Login failed:", response.status_code)

