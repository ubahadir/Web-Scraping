import datetime
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DE

website = "https://muhasebedemo.rahatfatura.com.tr/definitions/currents/customers"

d = DE.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver", desired_capabilities=d)
driver.maximize_window() # For maximizing window
# driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

driver.get(website)

username_box = driver.find_element(By.XPATH, '//*[@id="username"]')
username_box.send_keys("rahat_test1")
password_box = driver.find_element(By.XPATH, '//*[@id="password"]')
password_box.send_keys("12345678")
signIn_button = driver.find_element(By.XPATH, '//div[2]/div/form/button')
signIn_button.click()
rahatmuhasebe = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[1]/div/a/div')
rahatmuhasebe.click()
time.sleep(1)
donem2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/a/div/div')
donem2.click()
urunler = driver.find_element(By.XPATH, '//*[@id="def-items-nav"]/a/span')
driver.execute_script("arguments[0].click();", urunler)

def valueEntry(xpath, key):

    button = driver.find_element(By.XPATH, xpath)
    button.send_keys(key)

x = 45
a = 0
value = "1"

once = datetime.datetime.now()

stokkodu_path = '//*[@id="code"]'
stokadi_path = '//*[@id="name"]'
barkod_path = '//*[@id="barcode"]'
aciklama_path = '//*[@id="description"]'
alisfiyat_path = '//*[@id="purchase_price"]'
satisfiyat_path = '//*[@id="sales_price"]'

for i in range (1500):
    try: 
        x += 1
        a += 1
        
        time.sleep(2)

        yenistok_path = '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button'
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, yenistok_path))
        )

        yenistok_button = driver.find_element(By.XPATH, yenistok_path)

        try:            
            yenistok_button.click()
        except ElementClickInterceptedException as err:
            print (err)
            time.sleep(2)
            driver.execute_script["arguments[0].click();", yenistok_button]

        # driver.execute_script("arguments[0].click();", yenimusteri_button)
        # driver.execute_script("arguments[0].click();", element)

        anakayit_buton = driver.find_element(By.XPATH, '//*[@id="mainInfo-tab"]')
        anakayit_buton.click()

        valueEntry(stokkodu_path, x)
        valueEntry(stokadi_path, value)
        valueEntry(barkod_path, value)
        valueEntry(aciklama_path, value)

        fiyatlar_buton = driver.find_element(By.XPATH, '//*[@id="priceInfo-tab"]')
        fiyatlar_buton.click()

        valueEntry(alisfiyat_path, value)
        valueEntry(satisfiyat_path, value)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="new-item-form"]/div[3]/button'))
        )

        kaydet_buton = driver.find_element(By.XPATH, '//*[@id="new-item-form"]/div[3]/button')
        kaydet_buton.click()
        # time.sleep(2)
    except UnexpectedAlertPresentException as err:
        try:
            print ("Hata açıklaması:\n" + err.alert_text + "\n")
            error_time = datetime.datetime.now()
            print (once)
            print (error_time)
            print("Toplam " + str(a) + " kayit oluşturuldu.")
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(5)
            
        except NoAlertPresentException:             
            driver.refresh()
            print ("Error Occured. Refreshing the page")
            time.sleep(5)

    except:
        driver.refresh()
        print ("\nError Occured. Refreshing the page")
        time.sleep(5)

print(f"İşlem tamamlandı.\nToplam {a} kayıt oluşturuldu.\n")
sonra = datetime.datetime.now()

print (f"İşlem başlangıç zamanı: {once}")
print (f"İşlem bitiş zamanı: {sonra}")

for entry in driver.get_log('browser'):
    print(entry)
