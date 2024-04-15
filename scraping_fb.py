from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from random import uniform

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
#driver.maximize_window()

# definisco le strutture in cui immagazzinerò i dati
post = {
        'id': None,
        'date': None,
        'header': None,
        'image': None,
        'reactions': {
                'Mi piace': 0,
                'Love': 0,
                'Abbraccio': 0,
                'Ahah': 0,
                'Wow': 0,
                'Sigh': 0,
                'Grrr': 0
            },
        'commenti': []
       }
commento = {
    'id': None,
    'autore': None,
    'contenuto': None,
    'risposte': []
}

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
#time.sleep(uniform(1, 2))
time.sleep(5)

# timeline
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
timeline = driver.find_element(By.CSS_SELECTOR, "div[data-pagelet=\"ProfileTimeline\"]")
time.sleep(2)

# post
CSS_SELECTOR = '.' + '.'.join('x9f619 x1n2onr6 x1ja2u2z x1jx94hy x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld'.split())
post_elements = timeline.find_elements(By.CSS_SELECTOR, CSS_SELECTOR)
post_element = post_elements[2]
# post_element = timeline.find_element(By.CSS_SELECTOR, 'div:nth-of-type(1)')

# Javascript expression to scroll to a particular element
# arguments[0] refers to the first argument that is later passed
# in to execute_script method
# js_code = "arguments[0].scrollIntoView();"
# Execute the JS script
# driver.execute_script(js_code, post_element)

# data e id del post
CSS_SELECTOR = '.' + '.'.join('x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm'.split())
date = post_element.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
post['date'] = date.text
post_link = date.get_attribute("href")
post['id'] = post_link[post_link.find('&id=') + 4 : post_link.find('&id=') + 19]

# post_header
temp = post_element.find_element(By.CSS_SELECTOR, ".xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.x126k92a")
# xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a
post_header = temp.find_element(By.CSS_SELECTOR, "div > div")
post['header'] = post_header.text
time.sleep(uniform(1, 2))

# post_content
image = post_element.find_element(By.CSS_SELECTOR, "img")
source = image.get_attribute("src")
post['image'] = source

# lower_bar
lower_bar = post_element.find_element(By.CSS_SELECTOR, ".x6s0dn4.xi81zsa.x78zum5.x6prxxf.x13a6bvl.xvq8zen.xdj266r.xktsk01.xat24cr.x1d52u69.x889kno.x4uap5.x1a8lsjc.xkhd6sd.xdppsyt")
comments_element = lower_bar.find_element(By.XPATH, "//span[contains(text(), 'comments')]")

# comments_popup
time.sleep(10)
comments_element.click()
CSS_SELECTOR = '.' + '.'.join('x1n2onr6 x1ja2u2z x1afcbsf xdt5ytf x1a2a7pz x71s49j x1qjc9v5 xrjkcco x58fqnu x1mh14rs xfkwgsy x78zum5 x1plvlek xryxfnj xcatxm7 xrgej4m xh8yej3'.split())
time.sleep(uniform(1, 2))
comments_popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))

# comments
CSS_SELECTOR = '.' + '.'.join('x169t7cy x19f6ikt'.split())
#i = 1
#while True:
comment_element = WebDriverWait(comments_popup, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
commento['id'] = 0
CSS_SELECTOR = '.' + '.'.join('x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u'.split())
commento['autore'] = comment_element.find_element(By.CSS_SELECTOR, CSS_SELECTOR).text
CSS_SELECTOR = '.' + '.'.join('x1lliihq xjkvuk6 x1iorvi4'.split())
commento['contenuto'] = comment_element.find_element(By.CSS_SELECTOR, CSS_SELECTOR).text
print(post)
print(commento)

#comments_element = driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR)
#print(len(comments_element))
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# while True:
 #   super_comments = comments_popup.find_elements(By.CSS_SELECTOR, CSS_SELECTOR)
  #  time.sleep(uniform(1, 2))
  #  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(6000)
