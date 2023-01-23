from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os


def click(xpath):

    x = driver.find_element(By.XPATH, xpath)
    x.click()

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

#okunmamış mesjları tıklıyor
filter_unread = '//*[@id="side"]/div[1]/div/button/div/span'
click(filter_unread)
time.sleep(1)
#okunmamış kişiyi tıklıyor ve chat sayfasının açılmasını ve ayrıca 1 saniye bekliyor
unread_contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]')

day = ""
messages = []
contact = []

#oknumamış bir kişiyi tıklıyor
unread_contact.click()
time.sleep(2)

# WebDriverWait(driver, 5).until(
#     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[1]/div[1]'))
# )
#mesajları seçiyor
# messages1 = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span[1]/span')
# message_times1 = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/span')
messages_and_times = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[1]')
# message_times2 = messages_and_times.find_elements(By.XPATH, './div[2]/span')
# messages2 = messages_and_times.find_elements(By.XPATH, './div[1]/span/span')
msg_datetime = []
msgs = []

for a in messages_and_times:
    try:
        date_time = a.find_element(By.XPATH, './div[1]').get_attribute('data-pre-plain-text')
        msg_datetime.append(date_time)
        # y = a.find_element(By.XPATH, './div[1]/div').text
        message = a.text
        msgs.append(message)
        msg_id = 
    except:
        pass

for a,b in zip(msgs, msg_datetime):

    try:
        print (b + " " + a)
    except:
        pass
    # messages = []
    # msgtimes = []
    # messages = a.find_element(By.XPATH, './div[1]/span/span')
    # msgtimes = a.find_element(By.XPATH, './div[2]/span')

# for message,msgtime in zip(messages, msgtimes):

#     print ("Mesaj: \n")
#     print (message.text)
#     print (msgtime.text)""