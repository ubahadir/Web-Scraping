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
rahatmuhasebe.click()
time.sleep(1)
donem2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/a/div/div')
donem2.click()
time.sleep(1)

#ürünler
urunler = driver.find_element(By.XPATH, '//*[@id="def-items-nav"]/a/span')
urunler.click()
time.sleep(1)
#yeni_stok
yeni_stok = driver.find_element(By.XPATH, '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button')
yeni_stok.click()
time.sleep(1)
#stok kodu
x=1
x+=1
stok_kodu = driver.find_element(By.XPATH, '//*[@id="code"]')
stok_kodu.send_keys(x)
#stok adı
stok_adi = driver.find_element(By.XPATH, '//*[@id="name"]')
stok_adi.send_keys("a")
#barkod
barkod = driver.find_element(By.XPATH, '//*[@id="barcode"]')
barkod.send_keys("b")
#aciklama
aciklama = driver.find_element(By.XPATH, '//*[@id="description"]')
aciklama.send_keys("c")

#tanimlar kismi
#tanimlar = driver.find_element(By.XPATH, '//*[@id="definitionsInfo-tab"]')
#driver.execute_script("arguments[0].click();", tanimlar)
#time.sleep(2)
#kategori secimi bos olmali?
#marka-model girisleri yapilmali mi?
#birim secimi nasil yapilacak?

#fiyatlar kismi
fiyatlar = driver.find_element(By.XPATH, '//*[@id="priceInfo-tab"]')
fiyatlar.click()
time.sleep(1)
#alis fiyati -girdiğim veri önemli mi/değişmeli mi
alis_fiyati = driver.find_element(By.XPATH, '//*[@id="purchase_price"]')
alis_fiyati.send_keys("10")
#satis fiyati -girdiğim veri önemli mi/değişmeli mi
satis_fiyati = driver.find_element(By.XPATH, '//*[@id="sales_price"]')
satis_fiyati.send_keys("20")
#alış kdv satış kdv değiştirmeli miyim?

#kaydet
kaydet = driver.find_element(By.XPATH, '//*[@id="new-item-form"]/div[3]/button')
kaydet.click()

