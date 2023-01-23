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
unread_contacts = driver.find_elements(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]')
# unread_contacts.click()
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header')))
# time.sleep(1)

# %25 zoom out
# driver.execute_script("document.body.style.zoom='25%'")


# def sentBy(element):

#     sentby = element.find_element(By.XPATH, './div/div/div/span')
#     return sentby.text


day = ""
messages = []

# unread_contact.click()
# time.sleep (1)

# messagge_rows = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div')

# for row in messagge_rows:

#     print (row.text)

messages = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span[1]/span')
message_times = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/span')
messages_and_times = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[1]/div[1]/div//*[@id="main"]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[1]/div[1]/div')

for contact in unread_contacts:

    time.sleep(2)
    contact.click()
    searchbar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    searchbar.send_keys(Keys.NULL)
    WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header'))
    )
    time.sleep(1)
    messagge_rows = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div')
    

    # ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
    # your_element = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
    #             .until(expected_conditions.presence_of_element_located(
    #                 (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]/div')
    #                 )
    #                 )

    for row in messagge_rows:

        # if row.text == "TODAY":
        #     day = "TODAY"
        #     print ("Today")
        # elif row.text == "YESTERDAY":
        #     day = "YESTERDAY"
        #     print ("Yesteraday")
        # elif row.text == "MONDAY":
        #     day = "MONDAY"
        # elif row.text == "TUESDAY":
        #     day = "TUESDAY"
        # elif row.text == "WEDNESDAY":
        #     day = "WEDENSDAY"
        # elif row.text == "THIRSDAY":
        #     day = "THIRSDAY"
        # elif row.text == "FRIDAY":
        #     day = "FRIDAY"
        # elif row.text == "SATURDAY":
        #     day = "SATURDAY"
        # elif row.text == "SUNDAY":
        #     day = "SUNDAY"
        # else:
            # print(row.text)

        if day == "TODAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_today =[]
                if not sentby == "You:":
                    messages_today.append(row.text)
            except:
                pass
        elif day == "YESTERDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_yesterday =[]
                if not sentby == "You:":
                    messages_yesterday.append(row.text)
            except:
                pass
        elif day == "MONDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_monday =[]
                if not sentby == "You:":
                    messages_monday.append(row.text)
            except:
                pass
        elif day == "TUESDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_tuesday =[]
                if not sentby == "You:":
                    messages_tuesday.append(row.text)
            except:
                pass
        elif day == "WEDNESDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_wednesday =[]
                if not sentby == "You:":
                    messages_wednesday.append(row.text)
            except:
                pass
        elif day == "THIRSDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_thirsday =[]
                if not sentby == "You:":
                    messages_yesterday.append(row.text)
            except:
                pass
        elif day == "FRIDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_friday =[]
                if not sentby == "You:":
                    messages_friday.append(row.text)
            except:
                pass
        elif day == "SATURDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_saturday =[]
                if not sentby == "You:":
                    messages_saturday.append(row.text)
            except:
                pass
        elif day == "SUNDAY":
            try:
                sentby_elem = row.find_element(By.XPATH, './div/div/div/span')
                sentby = sentby_elem.get_attribute("aria-label")
                messages_sunday =[]
                if not sentby == "You:":
                    messages_sunday.append(row.text)
            except:
                pass

try:
    print ("Bugün:")
    print (messages_today)
except:
    pass
try:
    print ("Dün:")
    print (messages_yesterday)
except:
    pass
try:
    print ("Pazartesi:")
    print (messages_monday)
except:
    pass
try:
    print ("Salı:")
    print (messages_tuesday)
except:
    pass
try:
    print ("Çarşamba:")
    print (messages_wednesday)
except:
    pass
try:
    print ("Perşembe:")
    print (messages_thirsday)
except:
    pass
try:
    print ("Cuma:")
    print (messages_friday)
except:
    pass
try:
    print ("Cumartesi:")
    print (messages_saturday)
except:
    pass
try:
    print ("Pazar:")
    print (messages_sunday)
except:
    pass
# print(contact_messages.text)


# for message in contact_messages:

#     messages.append(message.text)
#     print (message.text)
    
# print (messages)
