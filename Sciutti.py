import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

url = "http://"+ input("Enter a URL: ")

print("Current working directory:", os.getcwd())

driver = webdriver.Firefox()

driver.get(url)

html = driver.page_source

# Write the HTML to a file
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)

try:
    cookies = driver.get_cookies()
    if cookies:
        with open('cookie.txt', 'w') as f:
            for cookie in cookies:
                f.write(str(cookie) + "\n")
        print("File 'cookie.txt' created successfully.")
    else:
        print("No cookies found")
except Exception as e:
    print("Error creating cookie file:", str(e))

driver.quit()

input("Press Enter to close...")