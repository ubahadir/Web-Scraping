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
#options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
driver.maximize_window() # For maximizing window
# driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

def click(url_name, xpath):

    url_name = driver.find_element(By.XPATH, xpath)
    url_name.click()


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

#alislar
alislar = driver.find_element(By.XPATH, '//*[@id="move-purchases-nav"]/a')
alislar.click()
time.sleep(1)

#yeni_alis
yeni_alis = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div[2]/a/button/span')
yeni_alis.click()
time.sleep(1)

#cari_sec
cari_sec = driver.find_element(By.XPATH, '//*[@id="supplier-name"]')
cari_sec.click()
time.sleep(1)

#tedarikci_cari_ara
cari_ara = driver.find_element(By.XPATH, '//*[@id="select2-supplier-select-container"]')
cari_ara.click()
time.sleep(1)

#tedarikci_cari_sec
tedarikci_cari_sec = driver.find_element(By.XPATH, '//*[@id="supplier-select-modal"]/div/div/div[2]/div/span[2]/span/span[1]/input')
tedarikci_cari_sec.send_keys("11")
tedarikci_cari_sec.send_keys(Keys.ENTER)
time.sleep(1)

#devam
devam = driver.find_element(By.XPATH, '//*[@id="select-supplier-button"]')
devam.click()
time.sleep(1)

#faturaya_tikla
fatura = driver.find_element(By.XPATH, '//*[@id="details"]/div[2]/form/div/div[1]/div[1]/label/span')
fatura.click()
time.sleep(1)

#yeni_satir
yeni_satir = driver.find_element(By.XPATH, '//*[@id="lines-add-row"]')
yeni_satir.click()
time.sleep(1)



# driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
# time.sleep(4)
# #tipi
# tipi = driver.find_element(By.XPATH, '//*[@id="myGrid"]/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]')
# driver.execute_script("arguments[0].click();", tipi)

# #stok seç
# stoksec_path = '//*[@id="select2-itemname-select-results"]/li[1]'
# WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, stoksec_path))
# )
# stok_sec = driver.find_element(By.XPATH, '//*[@id="select2-itemname-select-results"]/li[1]')
# stok_sec.click()
#stoğu seçmek için tekrar tıkla
# driver.execute_script("arguments[0].click();", tipi)
# tipi.send_keys(Keys.ARROW_UP)
# tipi.send_keys(Keys.ENTER)