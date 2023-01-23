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

#oknumamış bir kişiyi tıklıyor
unread_contact.click()
time.sleep(2)

#konuşma penceresindeki tüm rowları seçiyor
all_rows = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div/div')

msg_IDs = []
messages = []
msg_dates_persons = []
new_contact = []

for row in all_rows:
    # try:
    #     list_item = row.get_attribute('class')
    #     if "focusable-list-item" in list_item:
    #         print ("This is a list item")
    #         print (row.text)
    # except:
    #     pass
    #numara ile birlikte bir id oluştur mesaj idlerini alıyor,iletilmeyen normal mesajları ve mesaj tarihlerini alıyor
    try:
        msg_idx = row.find_element(By.XPATH, './div[1]').get_attribute('data-id').split('_')
        msg_id = msg_idx[2]
        msg_IDs.append(msg_id)
    except:
        msg_IDs.append("id yok")
    try:
        msg_date_person = row.find_element(By.XPATH, './div/div/div[1]/div/div[1]').get_attribute('data-pre-plain-text')
        msg_dates_persons.append(msg_date_person)
    except:
        msg_dates_persons.append("tarih yok")
    try:
        image_true = row.find_element(By.XPATH, ".//*[@data-testid='image-thumb']")
        image_url = image_true.find_element(By.XPATH, './div/div[2]/img').get_attribute('src')
        messages.append(image_url)
    except:
        pass
    try:
        message = row.find_element(By.XPATH, ".//*[@dir='ltr']/span").text
        messages.append(message)
    except:
        messages.append("mesaj yok")

        # print(msg_date_person + " ")
        # print(message)

for id,date,msg in zip(msg_IDs,msg_dates_persons,messages):
    print (f"ID: {id}, Date: {date}, Message: {msg}")


for row in all_rows:
    #mesaj idlerini çekiyor
    try:
        msg_idx = row.find_element(By.XPATH, './div[1]').get_attribute('data-id').split('_')
        msg_id = msg_idx[2]
        msg_IDs.append(msg_id)
    except:
        msg_IDs.append("ID yok")
    #mesajları çekiyor

    #mesaj eğer döküman ise mesaja document yazıyor
    try:
        document_elem = row.find_element(By.XPATH, './/div/button').get_attribute('data-testid')
        link_elem = row.find_element(By.XPATH, ".//*[@data-testid='link-description']").get_attribute('data-testid')
        contact_elem = row.find_element(By.XPATH, ".//*[@data-testid='vcard-msg']").get_attribute('data-testid')
        quote_elem = row.find_element(By.XPATH, ".//*[@data-testid='quoted-message']").get_attribute('data-testid')
        #döküman gönderilmişse mesaja document yazıyor
        if document_elem == "document-thumb":
            messages.append("document")
        #link atılmışsa linki mesaja dönüştürüyor
        elif link_elem == "link-description":
            link = row.find_element(By.XPATH, './/span//a').text
            messages.append(f"Link: {link}")
        # yeni kişinin telefon ve kişi bilgisini mesaj olarak gösterme
        # elif contact_elem == 'vcard-msg':
        #     driver.execute_script("arguments[0].click();", contact_elem)
        #     contact_name = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/span').text
        #     contact_numbers = driver.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]')
        #     for number in contact_numbers:
        #         new_contact.append(number.text)
    except:
        pass

    
