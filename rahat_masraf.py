import datetime
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
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
varliklar = driver.find_element(By.XPATH, '//*[@id="def-assets-nav"]/a/span')
driver.execute_script("arguments[0].click();", varliklar)
masraflar = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div/div[2]/a/button')
masraflar.click()


#buraya kadar carilere giriyor


def valueEntry(xpath, key):

    button = driver.find_element(By.XPATH, xpath)
    button.click()
    button.send_keys(key)

value = "1"

varlikkodu_xpath = '//*[@id="code"]'
varlikadi_xpath = '//*[@id="name"]'
aciklama_xpath = '//*[@id="new-item-description"]'

x = "k1"
a = 0

once = datetime.datetime.now()

for i in range (1500):
    try: 
        
        time.sleep(2)

        yenimasraf_path = '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button'

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, yenimasraf_path))
        )

        yenimasraf_buton = driver.find_element(By.XPATH, yenimasraf_path)

        try:
            driver.execute_script("arguments[0].click();", yenimasraf_buton)

        except ElementClickInterceptedException as err:
            print (err)           
            yenimasraf_buton.click()
        
        except ElementNotInteractableException as err:
            print (err)
            time.sleep(5)
            driver.execute_script("arguments[0].click();", yenimasraf_buton)

        x = x[0] + str(i)

        # varlik_kodu = driver.find_element(By.XPATH, '//*[@id="code"]')
        valueEntry(varlikkodu_xpath, x)
        valueEntry(varlikadi_xpath, value)
        valueEntry(aciklama_xpath, value)

        kaydet_buton = driver.find_element(By.XPATH, '//*[@id="new-expense-form"]/div[3]/button')
        kaydet_buton.click()
        # time.sleep(2)
        a += 1

    except UnexpectedAlertPresentException as err:
        try:
            print ("Hata açıklaması:\n" + err.alert_text + "\n")
            error_time = datetime.datetime.now()
            print (once)
            print (error_time)
            print("Toplam " + str(a) + " kayit oluşturuldu.")
            alert = driver.switch_to.alert
            alert.dismiss()
            time.sleep(5)
            
        except NoAlertPresentException:             
            driver.refresh()
            time.sleep(5)
    
    except ElementNotInteractableException as err:

        print ("Çok hızlı")
        driver.refresh()
        time.sleep(2)
        # x = x[0] + str(i + 1)

    except:
        
        driver.refresh()
        print ("Error Occured. Refreshing the page")
        time.sleep(2)

print("\nToplam " + str(a) + " kayit oluşturuldu.\n")
sonra = datetime.datetime.now()

print (once)
print (sonra + "\n")

for entry in driver.get_log('browser'):
    print(entry)


    # try:

    #     time.sleep(1)

    #     yeni_musteri = driver.find_element(By.XPATH, '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button')
    #     yeni_musteri.click()

    # except selenium.common.exceptions.UnexpectedAlertPresentException:

    #     print ("Sunucu Hatası")

    #     error_time = datetime.datetime.now()

    #     print (error_time)
        
    #     try:
    #         yenimusteri_xpath = '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button'
    #         element = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable(By.XPATH, yenimusteri_xpath)
    #             )
    #     except:   
