# basato sul video yt al link https://www.youtube.com/watch?v=rDBho83SUrw

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from datetime import datetime
from random import uniform
from bs4 import BeautifulSoup
import csv
import comments_module

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

post_id_list = []
y = 500

# apro l'url
url = "https://www.facebook.com/p/CRA-Agricoltori-traditi-100075537623150/"
driver.get(url)
time.sleep(uniform(1, 2))

# accetto i cookie
cookie_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Consenti tutti i cookie')]")
actions = ActionChains(driver)
actions.move_to_element(cookie_button)
actions.click(cookie_button)
actions.perform()
time.sleep(uniform(1, 2))

# inserisco email e password
fb_password = 'diegoegianlucavsfb200'
fb_email = 'gianluca.pisa.rainbow@gmail.com'
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

# metto i commenti in un csv
output_file = "Facebook\csv_docs\posts.csv"
with open(output_file, 'a', encoding='utf-8', newline='') as handle_w:
    csv_writer = csv.writer(handle_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    headers = ["post_id", "url", "date", "time_of_fetching", "header", "content", "image", "video", "likes"]
    csv_writer.writerow(headers)

    i = 0
    while True:

        soup = BeautifulSoup(driver.page_source, "html.parser")
        all_posts = soup.find_all("div", {"class": "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"})
        driver.switch_to.new_window('tab')
        for post in all_posts:
            # estraggo il post id, url 
            try:
                date_element = post.find("a", {"class": "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"})
                url = date_element["href"]
                post_id = url[url.find('?story_fbid=') + 12 : url.find('&id=')]
                if post_id in post_id_list:
                    continue
            except:
                post_id = None
                url = None
            post_id_list.append(post_id)
            # estraggo la data
            try:
                date_element = post.find("a", {"class": "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"})
                date = date_element["aria-label"]
            except:
                date = None
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
            csv_writer.writerow([post_id, url, date, datetime.now(), header, content, image, video, likes])
            # apro il link della data per estrarre i commenti
            try: 
                comments_module.get_comments(driver=driver, url=url, post_id=post_id)
                '''driver.get(url)
                # aspetto di essere dentro
                CSS_SELECTOR = '.' + '.'.join("x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1rg5ohu x1a2a7pz x1hc1fzr x1k90msu x6o7n8i xbxq160".split())
                wait = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))'''
                time.sleep(uniform(1, 3))
            except:
                pass
        driver.close()
        driver.switch_to.window(original_window)
        i = i + 1
        if i == 2:
            break
        for i_scroll in range(0, 10):
            driver.execute_script("window.scrollTo(0, "+ str(y) +")")
            y = y + 500
            time.sleep(uniform(0, 1))
        time.sleep(uniform(4, 6))
       
