from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DE
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# enable browser logging
d = DE.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver", desired_capabilities=d)
# driver.maximize_window() # For maximizing window

website = "https://www.google.com"


# load the desired webpage
driver.get(website)



# input()

# for i in range (5):
#     try:
#         searchbar = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')    
#         searchbar.send_keys("1234")

#     except UnexpectedAlertPresentException as err:

#         try:
#             print ("Hata açıklaması:\n" + err.alert_text)
#             alert = driver.switch_to.alert
#             alert.dismiss()
#             time.sleep(2)
#         except NoAlertPresentException:
#             print ("No Alert")
            





# print ("Press enter to see the log file")
# input()

# # print messages
# for entry in driver.get_log('browser'):
#     print(entry)