from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time

option1 = Options()
option1.add_argument("--disable-notifications")

html_file_path = "C:/Users/mayan/PycharmProjects/mumbai housing web scrape/practice.html"  # Replace with the actual file path
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
# Extract links from the HTML content
links = html_content.strip().split('\n')
# Parse the HTML content using BeautifulSoup
#print(html_content)

driver = webdriver.Chrome(executable_path='C:/Users/mayan/Desktop/chromedriver.exe',chrome_options=option1)
driver.maximize_window()
#
data_list = []
#
for idx, link in enumerate(links):
    driver.get(link)
    time.sleep(0.5)
    h1=driver.find_elements(By.CSS_SELECTOR, "h1")
    data_list = []

    for t in h1:
        data = t.text
        data_list.append(data)
    driver.quit()
print(data_list)
    # Print the fetched data

#print(data_list)
#https://www.nobroker.in/gurgaon/buy
#height = driver.execute_script('return document.body.scrollHeight')
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(1)