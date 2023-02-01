import os
import time
# import pandas as pd
from sqlalchemy import create_engine as ce
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, MetaData, select, text, and_, delete, ForeignKey, insert, UniqueConstraint
from sqlalchemy.exc import IntegrityError
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options.add_argument(
    r"user-data-dir={}".format(profile))

driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
actions = ActionChains(driver)

website = "https://web.whatsapp.com/"

driver.get(website)

def click(xpath):

    x = driver.find_element(By.XPATH, xpath)
    x.click()

# print ("Please Scan QR code and click enter")
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span'))
)
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

for contact in unread_contacts:

    msg_IDs = []
    messages = []
    msg_dates = []

    #oknumamış bir kişiyi tıklıyor
    contact.click()
    time.sleep(2)
    #kişi bilgisini tıklıyor
    contact_info = '//*[@id="main"]/header/div[2]/div[1]/div/span'
    click(contact_info)
    

    WebDriverWait(driver,5).until(
        EC.visibility_of_element_located((By.XPATH, '//header/div/div[2]/h1'))
    )

    business = "This is a business account."
    contact = driver.find_element(By.XPATH, '//header/div/div[2]/h1').text
    if "Contact" in contact:
        try:
            group = False
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//section/div[1]/div[2]/h2/span'))
            )
            contact_name = driver.find_element(By.XPATH, '//section/div[1]/div[2]/h2/span').text
            contact_number = driver.find_element(By.XPATH, '//section/div[1]/div[2]//span').text
            exit_contact = '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span'
            click(exit_contact)
        except TimeoutException:
        
            #business account ibaresi olmasını bekliyor ve teyit ediyor.
            WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, '//section/div[2]/div/div/div[1]'), business)
            )

            group = False
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//section/div/div[2]/div/div/span/span'))
            )
            contact_name = driver.find_element(By.XPATH, '//section/div/div[2]/div/div/span/span').text
            contact_number = driver.find_element(By.XPATH, '//section/div/div[3]/div/div/span/span').text

            exit_contact = '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span'
            click(exit_contact)

    
    else:
        exit_contact = '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span'
        click(exit_contact)
        group = True

    if group == False:
        #konuşma penceresindeki tüm rowları seçiyor
        all_rows = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div/div')

        for row in all_rows:
            
            #gelen veri türüne göre seçim yapmak için değişken oluşturup eğer varsa değişkene değer atıyor
            try:
                document_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='document-thumb']").get_attribute('data-testid')
            except NoSuchElementException:
                document_elem = None
            try:
                link_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='link-description']").get_attribute('data-testid')
            except NoSuchElementException:
                link_elem = None
            try:
                contact_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='vcard-msg']").get_attribute('data-testid')
            except NoSuchElementException:
                contact_elem= None
            try:
                quote_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='quoted-message']").get_attribute('data-testid')
            except NoSuchElementException:
                quote_elem = None
            try:
                location_elem = row.find_element(
                    By.CLASS_NAME, 'r8dz3'
                ).get_attribute('class')
            except NoSuchElementException:
                location_elem = None
            try:
                image_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='image-thumb']").get_attribute('data-testid')
            except NoSuchElementException:
                image_elem = None
            try: 
                imagecaption_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='image-caption']").get_attribute('data-testid')
            except NoSuchElementException:
                imagecaption_elem = None
            try:
                album_elem = row.find_element(
                    By.XPATH, ".//*[@data-testid='image-album']").get_attribute('data-testid')
                image_elem = None
            except NoSuchElementException:
                album_elem = None
            # BU BÖLÜMDE MESAJI KATEGORİYE AYIRIP EKLİYOR
            # döküman gönderilmişse mesaja document yazıyor
            if document_elem == "document-thumb":
                messages.append("document")
            #link atılmışsa linki mesaja dönüştürüyor
            elif link_elem == "link-description":
                link = row.find_element(By.XPATH, './/span//a').text
                messages.append(f"Link: {link}")
            #alıntı mesajların önce alıntılarını sonra mesajın kendisni yazıyor
            elif quote_elem == "quoted-message":
                # quote = row.find_element(
                #     By.XPATH, "//*[@data-testid='quoted-message']//div//span[starts-with(@class,'quoted-mention')]"
                #     ).text
                quote = row.find_element(By.CLASS_NAME, '_37DQv').text
                # msgs = row.find_elements(By.XPATH, ".//*[@dir='ltr']/span")
                msg = row.find_element(By.CLASS_NAME, '_21Ahp').text
                messages.append(((f"Quote: {quote}", f"Message: {msg}")))
            #kişi gönderildiğinde kişi ismi ve telefonunu yazıyor
            elif contact_elem == 'vcard-msg':
                contact = row.find_element(By.XPATH, './/div/div/div/div/div[1]/div[2]')
                driver.execute_script("arguments[0].click();", contact)
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="app"]/div/span[2]//div//div[1]/div[2]/div[1]/div/span'))
                    )
                vcard_name = driver.find_element(
                    By.XPATH, '//*[@id="app"]/div/span[2]//div//div[1]/div[2]/div[1]/div/span'
                ).text
                vcard_numbers = driver.find_elements(
                    By.XPATH, '//*[@id="app"]/div/span[2]//div/div[2]/div/div/div[1]/div[1]'
                )
                number1 = None
                number2 = None

                for number in vcard_numbers:
                    if number1 != None:
                        number2 = number.text
                    number1 = number.text                
                messages.append(((f"New Contact: İsim: {vcard_name} Tel1: {number1} Tel2:{number2}")))
                quit_vcard = '//*[@id="app"]/div/span[2]/div//header/div/div[1]/div/span'
                click(quit_vcard)

            elif location_elem == 'r8dz3':
                location = row.find_element(By.CLASS_NAME, 'r8dz3').get_attribute('href')
                messages.append(f"Location: {location}")
            elif image_elem == 'image-thumb':
                try:
                    image = row.find_element(By.XPATH, './/div//div[2]/img').get_attribute('src')
                    if imagecaption_elem == 'image-caption':
                        caption = row.find_element(By.XPATH, './/*[@data-testid="image-caption"]').text
                        messages.append(f"Image: {image}, Caption: {caption}")
                    else:
                        messages.append(f"Image: {image}")                                
                    # try:
                    #     image_dwld = row.find_element(By.XPATH, './/*[@data-testid="media-url-provider"]')
                    #     image_dwld.click()
                    # except NoSuchElementException:
                    #     image_dwld = row.find_element(By.XPATH, './/*[@data-testid="media-state-download"]')
                    #     image_dwld.click()
                    # WebDriverWait(driver, 5).until(
                    #     EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div/div//div//div[2]/img'))
                    # )
                    # image = row.find_element(By.XPATH, './/div//div[2]/img').get_attribute('src')
                    # messages.append(f"Image: {image}")
                except:
                    messages.append("image")
            elif album_elem == 'image-album':
                messages.append("image album")
            #DÜZ MESAJI EKLİYOR
            
            else:
                try:
                    message = row.find_element(By.CLASS_NAME, "_21Ahp").text
                    messages.append(message)
                except NoSuchElementException:
                    pass
            #MESAJ IDLERİNİ ÇEKİYOR
            try:
                msg_idx = row.find_element(By.XPATH, './div[1]').get_attribute('data-id').split('_')
                msg_id = msg_idx[2]
                msg_IDs.append(msg_id)
            except NoSuchElementException:
                pass
            except AttributeError:
                pass
            #MESAJ TARİHLERİNİ ÇEKİYOR
            list_item = row.get_attribute('class')
            try:
                list_item2 = row.find_element(By.XPATH, './div').get_attribute('class')
            except:
                list_item2 = None

            if document_elem == 'document-thumb':
                msg_person = row.find_element(By.XPATH, './div/div/div/span').get_attribute('aria-label')
                msg_hour = row.find_element(By.XPATH, './div/div/div/div/div/div/span').text
                msg_dates.append(((msg_hour,msg_person)))
            # if contact_elem == 'vcard-msg':
            #     msg_date = row.find_element(
            #         By.XPATH, './div/div/div/div').get_attribute('data-pre-plain-text'
            #         )
            #     msg_dates.append(msg_date)
            elif album_elem == 'image-album':
                msg_dates.append("no date")
            # whatsapptaki gereksiz rowları ayıklıyor
            elif "focusable-list-item" in list_item:
                pass
            elif "focusable-list-item" in list_item2:
                pass
            elif "_1DlhQ _1JCqN" in list_item:
                pass                
            # gereksiz rowlar ayıklandıktan sonra mesaj tarihlerini çekiyor
            
            else:
            
                    try:
                        msg_date = row.find_element(
                            By.XPATH, './/*[@data-pre-plain-text]').get_attribute('data-pre-plain-text')
                        msg_dates.append(msg_date)
                    except:
                        msg_dates.append("no date")

        # meta = MetaData()
        # #tablo daha önceden oluşturuldu fakat burada ekleme işlemi yapmam için tekrar tanımlıyorum
        # whatsapp_deneme1 = Table(
        #     'whatsappdeneme1', meta,
        #     Column ('message id', String, unique=True, key='message_id'),
        #     Column ('date', String),
        #     Column ('message', String),
        #     Column ('number', String),
        #     Column ('id', Integer, primary_key = True)
        # )
    

        for msg, date, id in zip(messages, msg_dates, msg_IDs):

            print(id)
            print(date)
            print(msg)

        print (contact_name)
        print (contact_number)
    else:
        pass
        #database e bağlanıyor
        # pg_engine = ce("postgresql://postgres:5645645@localhost:5432/whatsapp_deneme", echo=True)
        # conn = pg_engine.connect()
        
        # #tabloya insert metodu ile veri ekleme
        # for id,date,msg in zip(msg_IDs,msg_dates, messages):
        #     # try:
        #     ins = whatsapp_deneme1.insert().values(message_id=id, date=date, message=msg, number=contact_number)
        #     result = conn.execute(ins)
        #     # except IntegrityError:
        #     #     pass
        
    

# driver.quit()

    # meta.create_all(pg_engine)


    # df = pd.DataFrame({'ID': msg_IDs, 'Date': msg_dates, 'Messages': messages})

    # print(df)
    # df.to_json('WhatsappDeneme.json')

    # conn = psycopg2.connect("dbname=whatsapp_deneme user=postgres password=5645645")
    # print(conn)

    # pg_engine = ce("postgresql://postgres:5645645@localhost:5432/whatsapp_deneme")

    # data = pd.read_json("WhatsappDeneme.json")

    # data.to_sql('whatsapp_deneme', pg_engine)


    # for row in all_rows:
        # try:
        #     list_item = row.get_attribute('class')
        #     if "focusable-list-item" in list_item:
        #         print ("This is a list item")
        #         print (row.text)
        # except:
        #     pass
        #numara ile birlikte bir id oluştur mesaj idlerini alıyor,iletilmeyen normal mesajları ve mesaj tarihlerini alıyor
