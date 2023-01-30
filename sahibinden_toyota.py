from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Topics: Locate a button, select element within dropdown and extract data from a table

# define the website to scrape and path where the chromediver is located
website = 'https://www.sahibinden.com/vasita?viewType=Gallery&query_text_mf=toyota&query_text=toyota'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.headless = True

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

path = 'Users/usAme/Downloads/chromedriver' # write the path here

# define 'driver' variable
# open Google Chrome with chromedriver
driver.get(website)

# bosluk = driver.find_element(By.CLASS_NAME, 'desktop win')

# bosluk.click()
# time.sleep(2)

toyota_liste_50_button = driver.find_element(By.XPATH, '//*[@id="searchResultsSearchForm"]/div/div[3]/div[4]/div[2]/ul/li[2]/a')

driver.execute_script("arguments[0].click();", toyota_liste_50_button)

time.sleep(3)

# arabalar = driver.find_elements(By.TAG_NAME, 'td')
ilanlar = driver.find_elements(By.CLASS_NAME, 'searchResultsClassifiedId')
ilan_baslik = driver.find_elements(By.CLASS_NAME, 'classifiedTitle')
ilan_fiyat = driver.find_elements(By.CLASS_NAME, 'classified-price-container')
ilan_tarih = driver.find_elements(By.XPATH, '//td/div[3]/div[1]')
ilan_konum = driver.find_elements(By.XPATH, '//td/div[3]/div[2]')

ilan_liste =[]
baslik_liste= []
fiyat_liste = []
tarih_liste = []
konum_liste = []
tarihh = []

for ilan in ilanlar:

    ilan_liste.append(ilan.text)


for baslik in ilan_baslik:

    baslik_liste.append(baslik.text)


for fiyat in ilan_fiyat:

    fiyat_liste.append(fiyat.text)


for tarih in ilan_tarih:

    tarih_liste.append(tarih.text)

for a in tarih_liste:

    tarihh.append(a[14:])

for konum in ilan_konum:

    konum_liste.append(konum.text[11:].strip())

time.sleep(10)
driver.quit()

df = pd.DataFrame({'İlan no': ilan_liste, 'İlan Başlık': baslik_liste, 'Fiyat': fiyat_liste, 'Tarih': tarihh, 'Konum': konum_liste})
df.to_csv('Sahibinden_Toyota.csv')
print(df)


# # locate a button
# all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
# # click on a button
# all_matches_button.click()
# # using the "box" section as a reference to help us locate an element inside
# box = driver.find_element_by_class_name('panel-body')
# # select dropdown and select element inside by visible text
# dropdown = Select(box.find_element_by_id('country'))
# dropdown.select_by_visible_text('Spain')
# # implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
# time.sleep(5)
# # select elements in the table
# matches = driver.find_elements_by_css_selector('tr')

# # storage in a list
# all_matches = [match.text for match in matches]

# #quit drive we opened in the beginning
# driver.quit()

# # Bonus: Create Dataframe in Pandas and export to CSV (Excel)
# df = pd.DataFrame({'goals': all_matches})
# print(df)
# df.to_csv('tutorial.csv', index=False)