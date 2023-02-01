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


website = "https://muhasebedemo.rahatfatura.com.tr/definitions/currents/customers"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
driver.maximize_window() # For maximizing window
# driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

driver.get(website)
kullanici_adi = driver.find_element(By.XPATH , '//*[@id="username"]')
kullanici_adi.send_keys("rahat_test1")
sifre = driver.find_element(By.XPATH, '//*[@id="password"]')
sifre.send_keys("12345678")
giris = driver.find_element(By.XPATH, '//div[2]/div/form/button')
driver.execute_script("arguments[0].click();", giris)
time.sleep(1)
rahatmuhasebe = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[1]/div/a/div')
driver.execute_script("arguments[0].click();", rahatmuhasebe)
time.sleep(1)
donem2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/a/div/div')
driver.execute_script("arguments[0].click();", donem2)
time.sleep(1)
varliklar = driver.find_element(By.XPATH, '//*[@id="def-assets-nav"]/a/span')
driver.execute_script("arguments[0].click();", varliklar)
time.sleep(1)
x=1395
for i in range(1000):
    yeni_varlik_olustur = driver.find_element(By.XPATH, '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button')
    driver.execute_script("arguments[0].click();", yeni_varlik_olustur)
    time.sleep(1)

    #kasa,banka,çek,senet arası seçim yaptırmam lazım(tek tek sırasıyla tıklamaları girmeli miyim,başka yolu var mı?)

    varlik_kodu = driver.find_element(By.XPATH, '//*[@id="code"]')
    x+=1
    varlik_kodu.send_keys(x)

    varlik_adi = driver.find_element(By.XPATH, '//*[@id="name"]')
    varlik_adi.send_keys("a")

    aciklama = driver.find_element(By.XPATH, '//*[@id="new-item-description"]')
    aciklama.send_keys("b")

    kaydet = driver.find_element(By.XPATH, '//*[@id="new-value-form"]/div[3]/button')
    driver.execute_script("arguments[0].click();", kaydet)
    time.sleep(3)















