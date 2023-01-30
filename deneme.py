import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

website = "https://www.sahibinden.com/bmw-1-serisi"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
driver.maximize_window() # For maximizing window
# driver.implicitly_wait(20) # gives an implicit wait for 20 seconds


driver.get(website)


# my_element_id = '//*[@id="categoryListContainer"]/div[1]/ul/li[3]/a'
# ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
# your_element = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
#                 .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))

# # bmw_tum = driver.find_element(By.XPATH, '//*[@id="categoryListContainer"]/div[1]/ul/li[3]/a')
# # driver.execute_script("arguments[0].click();", bmw_tum)

for handle in driver.window_handles:
    driver.switch_to.window(handle)