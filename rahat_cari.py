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
cariler = driver.find_element(By.XPATH, '//*[@id="def-currents-nav"]/a/span')
driver.execute_script("arguments[0].click();", cariler)

#buraya kadar carilere giriyor



def valueEntry(xpath, key):

    button = driver.find_element(By.XPATH, xpath)
    button.click()
    button.send_keys(key)

value = "1"
tc = "1111111111111"

unvan_path = '//*[@id="name"]'
tc_path = '//*[@id="tax_number"]'
vergi_dairesi_path = '//*[@id="tax_office"]'
adres_path = '//*[@id="address"]'
il_path = '//*[@id="city"]'
ilce_path = '//*[@id="district"]'
ulke_path = '//*[@id="country"]'
postakodu_path = '//*[@id="postal_code"]'
eposta_path = '//*[@id="email"]'
telefon_path = '//*[@id="phone_number"]'
aciklama_path = '//*[@id="description"]'
parabirimi_path = '//*[@id="currency_code"]'
adi_path = '//*[@id="person_name"]'
soyadi_path = '//*[@id="person_surname"]'
telno_path = '//*[@id="person_phone"]'
posta_path = '//*[@id="person_email"]'


x = 5500
a = 0

once = datetime.datetime.now()

for i in range (10000):
    try: 
        
        # time.sleep(2)

        yenimusteri_path = '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button'
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, yenimusteri_path))
        )

        yenimusteri_button = driver.find_element(By.XPATH, yenimusteri_path)

        try:            
            yenimusteri_button.click()
        except ElementClickInterceptedException as err:
            print (err)
            time.sleep(2)
            driver.execute_script["arguments[0].click();", yenimusteri_button]        

        # driver.execute_script("arguments[0].click();", yenimusteri_button)
        # driver.execute_script("arguments[0].click();", element)

        anakayit_buton = driver.find_element(By.XPATH, '//*[@id="mainInfo-tab"]')
        anakayit_buton.click()

        x += 1

        cari_kodu = driver.find_element(By.XPATH, '//*[@id="code"]')
        cari_kodu.click()
        cari_kodu.send_keys(x)

        valueEntry(unvan_path, value)
        valueEntry(tc_path, tc)
        valueEntry(vergi_dairesi_path, value)

        adres_buton = driver.find_element(By.XPATH, '//*[@id="addressInfo-tab"]')
        adres_buton.click()

        valueEntry(adres_path, value)
        valueEntry(il_path, value)
        valueEntry(ilce_path, value)
        valueEntry(ulke_path, value)
        valueEntry(postakodu_path, value)

        ekbilgiler_buton = driver.find_element(By.XPATH, '//*[@id="otherInfo-tab"]')
        ekbilgiler_buton.click()

        valueEntry(eposta_path, value)
        valueEntry(telefon_path, value)
        valueEntry(aciklama_path, value)
        valueEntry(parabirimi_path, value)

        kisi_buton = driver.find_element(By.XPATH, '//*[@id="peopleInfo-tab"]')
        kisi_buton.click()

        valueEntry(adi_path, value)
        valueEntry(soyadi_path, value)
        valueEntry(telno_path, value)
        valueEntry(posta_path, value)

        kaydet_buton = driver.find_element(By.XPATH, '//*[@id="new-customer-form"]/div[3]/button')
        kaydet_buton.click()
        # time.sleep(2)

        kaydetonay_xpath = '/html/body/div[8]/div/div[6]/button[1]'
        kaydetonay_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, kaydetonay_xpath))
        ).click()
        # kaydet_onay_buton = driver.find_element(By.XPATH, '/html/body/div[8]/div/div[6]/button[1]')
        # kaydet_onay_buton.click()

        a += 1

    except UnexpectedAlertPresentException as err:
        try:
            print ("Hata açıklaması:\n" + err.alert_text + "\n")
            error_time = datetime.datetime.now()
            print (f"Başlama zamanı: {once}")
            print (f"Hata zamanı: {error_time}")
            print("Toplam " + str(a) + " kayit oluşturuldu.")
            alert = driver.switch_to.alert
            alert.dismiss()
            time.sleep(5)
            
        except NoAlertPresentException:             
            driver.refresh()
            time.sleep(5)

    except:

        driver.refresh()
        print ("\nError Occured. Refreshing the page\n")
        time.sleep(5)

print(f"İşlem tamamlandı.\nToplam {a} kayıt oluşturuldu.\n")
sonra = datetime.datetime.now()

print (f"İşlem başlangıç zamanı: {once}")
print (f"İşlem bitiş zamanı: {sonra}")

for entry in driver.get_log('browser'):
    print(entry)
