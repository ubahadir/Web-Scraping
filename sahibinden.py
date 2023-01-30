import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

website = "https://www.sahibinden.com/alt-kategori/otomobil"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
driver.maximize_window() # For maximizing window
# driver.implicitly_wait(20) # gives an implicit wait for 20 seconds


driver.get(website)


my_element_id = '//*[@id="categoryListContainer"]/div[1]/ul/li[3]/a'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
your_element = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
                .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))

bmw_tum = driver.find_element(By.XPATH, '//*[@id="categoryListContainer"]/div[1]/ul/li[3]/a')
driver.execute_script("arguments[0].click();", bmw_tum)

bmw_modeller1 = driver.find_elements(By.XPATH, '//div/ul/li/div') # bmw modelleri en üst kategoriler listesini seçme

#50 sonuç göster butonu


altmodel_ilansayisi = [] #alt modellerin ilan sayilarini lisleteleme
Ilan_No = []
Model = []	
Ilan_Baslik = []
Yil = []
Kilometre = []	
Renk = []	
Fiyat = []	
Ilan_Tarih	= []
Konum = []


for bmw_model1 in bmw_modeller1:

    ilan_sayisi_span = bmw_model1.find_element(By.TAG_NAME, 'span').text
    ilan_sayisi = ilan_sayisi_span.replace('(', '').replace(')', '').replace('.', '')
    ilan_sayisi_int = int(ilan_sayisi)


    if ilan_sayisi_int <= 1000:       
        bmw_model_buton = bmw_model1.find_element(By.TAG_NAME, "a")
        driver.execute_script("arguments[0].click();", bmw_model_buton)
        driver.refresh()
        sonuc_50 = driver.find_element(By.XPATH, '//div/div[4]/div[3]/div[2]/ul/li[2]/a')
        driver.execute_script("arguments[0].click();", sonuc_50)
        time.sleep(2)
        ilanlar = driver.find_elements(By.XPATH, '//tbody/tr')

        for ilan in ilanlar:

            try:
                Ilan_No.append(ilan.get_attribute("data-id"))
                # ilan_model = ilan.find_element(By.XPATH, './td[2]')
                # Model.append(ilan_model.text)
                # ilan_baslik = ilan.find_element(By.CLASS_NAME, 'classifiedTitle')
                # Ilan_Baslik.append(ilan_baslik.text)
            except:
                pass
    
    else:

        pass
"""

    else:
        
        bmw_modeller1_link = bmw_model1.find_element(By.CLASS_NAME, 'allCategoryBottomLink') 
        driver.execute_script("arguments[0].click();", bmw_modeller1_link) #ilgili modelin 1000den fazla ilanı olduğu için tüm ilanlarına tıklıyoruz

        bmw_modeller2 = driver.find_elements(By.XPATH, '//*[@id="categoryListContainer"]/div/ul/li/div') #bir alt kategorideki tüm bmw alt modellerini seçiyor

        for bmw_model2 in bmw_modeller2:                       

            ilan_sayisi_span = bmw_model2.find_element(By.TAG_NAME, 'span').text
            ilan_sayisi = ilan_sayisi_span.replace('(', '').replace(')', '').replace('.', '')
            ilan_sayisi_int = int(ilan_sayisi)

            if ilan_sayisi_int > 1000:
                bmw_modeller2_link = bmw_model2.find_element(By.CLASS_NAME, 'allCategoryBottomLink')
                driver.execute_script("arguments[0].click();", bmw_modeller2_link)
                time.sleep(3)
         
"""

driver.quit()


#else:   
        # my_element_id = '//*[@id="categoryListContainer"]/div/ul/li/div/a'
        # ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
        # your_element = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
        #         .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))

## ilan sayisini int'e çevirme

# bmw_modeller = driver.find_elements(By.XPATH, '//*[@id="searchCategoryContainer"]/div/div[1]/ul/li')

# for bmw_model in bmw_modeller:

#     a = bmw_model.find_element(By.TAG_NAME, 'span').text
#     b = a.replace('(', '').replace(')', '').replace('.', '')
#     print (b)


##Lancia'ya tıklatmak için (çalışmıyor)
# for marka in otomobil_marka:

#     if "Lancia" in marka.text:

#         marka.click()

## Markaların listesini getirme
# markalar = []

# for marka in otomobil_marka:
    
#     markalar.append(marka.text)

# markalar.sort()

# print (markalar)


    
    
    