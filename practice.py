from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option1 = Options()
option1.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path='C:/Users/mayan/Desktop/New folder/chromedriver.exe',chrome_options=option1)
driver.maximize_window()
driver.get('https://www.nobroker.in/property/sale/gurgaon/multiple?searchParam=W3sibGF0IjoyOC40MTYwMjgxLCJsb24iOjc2Ljk5MTQzOTUsInBsYWNlSWQiOiJDaElKYllNRXZ0Z1hEVGtSVmRlRG9FM0N3QUEiLCJwbGFjZU5hbWUiOiJTZWN0b3IgMzYiLCJzaG93TWFwIjpmYWxzZX0seyJsYXQiOjI4LjQzNDY5OTMsImxvbiI6NzcuMDQzMDQ4MywicGxhY2VJZCI6IkNoSUpENTA3OUc0WURUa1I2cFFuS2pNQW1vYyIsInBsYWNlTmFtZSI6IlNlY3RvciAzOCIsInNob3dNYXAiOmZhbHNlfSx7ImxhdCI6MjguNDM3NTE2NSwibG9uIjo3Ni45OTk5NDc0LCJwbGFjZUlkIjoiQ2hJSnhZZ2EydkVYRFRrUi14VlVCLXdPT0RrIiwicGxhY2VOYW1lIjoiU2VjdG9yIDM3Iiwic2hvd01hcCI6ZmFsc2V9XQ==&radius=2.0&city=gurgaon&locality=Sector%2056,Sector%2051&nbFr=list_view')
#https://www.nobroker.in/gurgaon/buy
#height = driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(1)
driver.execute_script('window.scrollTo(20, document.body.scrollHeight)')
time.sleep(1)
driver.execute_script('window.scrollTo(20, document.body.scrollHeight)')
#driver.find_element(by=By.XPATH, value='//*[@id="appPortal"]/div/div[2]/div/div/div/div[3]/label').click()
time.sleep(0.5)
driver.execute_script('window.scrollTo(100, document.body.scrollHeight)')
time.sleep(0.5)
driver.execute_script('window.scrollTo(150, document.body.scrollHeight)')
time.sleep(1)
driver.execute_script('window.scrollTo(180, document.body.scrollHeight)')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="signUp-phoneNumber"]').send_keys('9228585477')#6
# time.sleep(1)
# Find a elements
a_elements = driver.find_elements(By.TAG_NAME, "a")

# Fetch href attributes and store them
href_list = []

for a_element in a_elements:
    href = a_element.get_attribute("href")
    if href:
        href_list.append(href)

# Close the WebDriver
driver.quit()



with open('practice.html', 'w', encoding='utf-8') as f:
    for href in href_list:
        f.write(href+"\n")
#Print the fetched href attributes
# for href in href_list:
#     print(href)
# html = driver.page_source
#
# with open('sector,36,37,38.html','w',encoding='utf-8') as f:
#       f.write(html)
#user_input = driver.find_element(by=By.XPATH, value='//*[@id="listPageSearchLocality"]')

