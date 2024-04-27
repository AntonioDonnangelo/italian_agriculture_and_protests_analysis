# ispirato al video yt al link https://www.youtube.com/watch?v=rDBho83SUrw

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime, date
import time
from random import uniform
from bs4 import BeautifulSoup
import csv
import comments_module
import os
import fbdate_to_date

# opzioni che servono a mascherare il fatto che il browser non è guidato da un umano
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# opzioni per chiudere automaticamente i pop up del browser
options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
        # with 2 should disable notifications
    },
)

# ozione per allargare la finestra a tutto lo schermo
options.add_argument("--start-maximized")

# instanzio il driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# apro l'url
url = "https://www.facebook.com/p/CRA-Agricoltori-traditi-100075537623150/"
# url = "https://www.facebook.com/TaylorSwift"
driver.get(url)
time.sleep(uniform(1, 2))

# accetto i cookie
cookie_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Consenti tutti i cookie')]")
actions = ActionChains(driver)
actions.move_to_element(cookie_button)
actions.click(cookie_button)
actions.perform()
time.sleep(uniform(1, 2))

# leggo da file email e password per facebook
with open("E:\Gianluca\Master Big Data Pisa\Progetto_Finale\Agricolo\Facebook\credentials.txt", 'r', encoding="utf-8") as file:
    line1 = file.readline()
    line1 = line1[0:-1]
    fb_password = line1.split()[2]
    line2 = file.readline()
    line2 = line2[0:]
    fb_email = line2.split()[2]

# inserisco email e password
credentials = driver.find_elements(By.CSS_SELECTOR, '.x1i10hfl.xggy1nq.x1s07b3s.x1kdt53j.x1a2a7pz.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.xzsf02u.x1uxerd5.x1fcty0u.x132q4wb.x1a8lsjc.x1pi30zi.x1swvt13.x9desvi.xh8yej3.x15h3p50.x10emqs4')
email_field = credentials[0]
psw_field = credentials[1]
email_field.send_keys(fb_email)
time.sleep(uniform(1, 2))
psw_field.send_keys(fb_password)
time.sleep(uniform(1, 2))

# clicco accedi
accedi_button = driver.find_element(By.CSS_SELECTOR, '.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1fq8qgq')
actions = ActionChains(driver)
actions.move_to_element(accedi_button)
actions.click(accedi_button)
actions.perform()

# fermo selenium finché la pagina non è carica
CSS_SELECTOR = '.' + '.'.join('x78zum5 x15sbx0n x5oxk1f x1jxijyj xym1h4x xuy2c7u x1ltux0g xc9uqle'.split())
wait = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
time.sleep(uniform(4, 6))
original_window = driver.current_window_handle

# inserisco i (post_date, date_count) già visitati in date_list
try:
     with open("E:\Gianluca\Master Big Data Pisa\Progetto_Finale\Agricolo\Facebook\csv_docs\posts.csv", 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        date_list = []
        for row in reader:
            try:
                temp_date = date.fromisoformat(row["post_date"])
            except:
                temp_date = row["post_date"]
            try:
                temp_date_count = int(row["date_count"])
            except:
                temp_date_count = row["date_count"]
            date_list.append((temp_date, temp_date_count))
except:
    date_list = []
initial_length = len(date_list)
y = 500 # costante iniziale per lo scorrimento della pagina
number_new_posts = 50 # quanti nuovi post voglio 

# metto i commenti in un csv
output_file = "E:\Gianluca\Master Big Data Pisa\Progetto_Finale\Agricolo\Facebook\csv_docs\posts.csv"
with open(output_file, 'a', encoding='utf-8', newline='') as handle_w:
    csv_writer = csv.writer(handle_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    # se il file è vuoto lungo la prima riga metto l'header
    file_size = os.path.getsize("E:\Gianluca\Master Big Data Pisa\Progetto_Finale\Agricolo\Facebook\csv_docs\posts.csv")  # Find the size of csv file
    if file_size == 0:     # if size is empty 
        headers = ["url", "post_date", "date_count", "time_of_fetching", "header", "content", "image", "video", "likes"]
        csv_writer.writerow(headers)

    # estraggo i dati dai post
    if len(date_list) == 0:
        previous_date = None
    else:
        previous_date = date_list[-1][0]
    if len(date_list) == 0:
        date_count = 1
    else:
        date_count = date_list[-1][1]
    while True:

        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_posts = soup.find_all("div", {"class": "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"})
        driver.switch_to.new_window('tab')        
        for post in all_posts:
            # estraggo la data
            try:
                date_element = post.find("a", {"class": "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"})
                post_date = date_element["aria-label"].strip()
            except:
                post_date = None
            # se il post è dell'ultima settimana salto l'iterazione
            if post_date is not None and len(post_date) <= 3:
                continue
            # trasformo la data in un oggetto di tipo date yyyy-mm-dd
            try:
                if post_date is not None and post_date != '':
                    post_date = fbdate_to_date.string_to_date(post_date)
            except:
                pass
            # aggiorno date count
            if post_date == previous_date:
                date_count = date_count + 1
            else:
                date_count = 1
            previous_date = post_date
            # se ho già visto il post salto l'iterazione
            if (post_date, date_count) in date_list:
                continue
            # estraggo l'url 
            try:
                date_element = post.find("a", {"class": "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"})
                url = date_element["href"]
            except:
                url = None
            # estraggo il numero di like
            try:
                likes = post.find("span", {"class": "xt0b8zv x2bj2ny xrbpyxo xl423tq"}).text
            except:
                likes = None
            # estraggo il contenuto dell'header
            try:
                header = post.find("div", {"class": "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"}).text
            except:
                header = None
            # estraggo il contenuto del post
            try:
                content = post.find("div", {"class": "x1yx25j4 x13crsa5 x6x52a7 x1rxj1xn xxpdul3"}).text
            except:
                content = None
            # estraggo l'immagine del post
            try:
                image = post.find("img", {"class": "x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3 xl1xv1r"})["src"]
            except:
                image = None
            # estraggo il video del post
            try:
                video = post.find("video", {"class": "x1lliihq x5yr21d xh8yej3"})["src"]
            except:
                video = None
            # scrivo su csv i dati che ho raccolto
            check_list = [url, post_date, header, content, image, video, likes]
            if any(element is not None and element != '' for element in check_list):
                date_list.append((post_date, date_count))
                csv_writer.writerow([url, post_date, date_count, datetime.now(), header, content, image, video, likes])
            # apro il link della data per estrarre i commenti
            try: 
                comments_module.get_comments(driver=driver, url=url, post_date=post_date, post_date_count=date_count)
            except:
                pass
            if (len(date_list) - initial_length) >= number_new_posts:
                break
        driver.close()
        driver.switch_to.window(original_window)
        #print(len(date_list) - initial_length)    
        if (len(date_list) - initial_length) >= number_new_posts:
            break
        for i_scroll in range(0, 10):
            driver.execute_script("window.scrollTo(0, "+ str(y) +")")
            y = y + uniform(400, 600)
            time.sleep(uniform(0, 1))
        time.sleep(uniform(4, 6))

       
       
