from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options.add_argument(
    r"user-data-dir={}".format(profile))

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")

website = "https://web.whatsapp.com/"

driver.get(website)

print ("Please Scan QR code and click enter")
input()
print("Logged In")

my_element_id = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
your_element = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
                .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))

search_bar = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
# driver.execute_script("arguments[0].click();", search_bar)

# search_bar.click()

liste = ["+905556277992", "+905054924088", "+905071118596"]
numaram = "+905556277992"

# for numara in liste:

#     search_bar.send_keys(numara)

#     time.sleep(6)

#     search_result = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]/div')
#     search_result.click()
#     msg = input("Type your message here: ")
#     type_message = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
#     type_message.send_keys(msg)
#     type_message.send_keys(Keys.ENTER)

for numara in liste:

    new_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]/div/span')
    new_button.click()
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]')
    search_box.send_keys(numara)
    time.sleep(1)
    contact_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/div[1]/span[1]')
    contact_button.click()
    msg = input("Type your message here: ")
    type_message = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    type_message.send_keys(msg)
    type_message.send_keys(Keys.ENTER)

# try:

#     search_result_true = driver.find_element(By.CLASS_NAME, "_1Oe6M")
#     # search_result = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]/div[1]/div[1]/span[1]')
#     element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]/div[1]/div[1]/span[1]')))
#     driver.execute_script("arguments[0].click();", search_result)
#     search_result.click()
# except:

#     print ("Error")

# first_elem = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]')    
# second_elem = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]/div[2]/div[1]/span/span')
# third_elem = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]/div[1]/div[1]/span[1]')


# try:
#     first_elem.click()
#     print ("First element is clickable")
    
# except:
#     print ("First element is not clickable")

# try:
#     second_elem.click()
#     print ("Second element is clickable")
    
# except:
#     print ("Second element is not clickable")

# try:
#     third_elem.click()
#     print ("Third element is clickable")
    
# except:
#     print ("Third element is not clickable")


#chat listesi
# chat_list = driver.find_elements(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div')


# for chat_person in chat_list:
    
#     cpersonName = chat_person.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span/span')
#     if dosya in cpersonName.text:

#         driver.execute_script("arguments[0].click();", cpersonName)
#         my_element_id = 'selectable-text copyable-text'
#         ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
#         your_element = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
#                 .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, my_element_id)))
#         type = driver.find_element(By.CLASS_NAME, 'selectable-text copyable-text')
#         type.send_keys("1").send_keys(Keys.ENTER)

#     else:
#         pass

