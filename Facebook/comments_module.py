# x78zum5 x1w0mnb xeuugli classi css per espandere le risposte e view more replies

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from datetime import datetime
from random import uniform
from bs4 import BeautifulSoup
import csv

def get_comments(driver, url, post_id):

    # apro l'url
    driver.get(url)

    # aspetto di essere dentro
    CSS_SELECTOR = '.' + '.'.join("x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1rg5ohu x1a2a7pz x1hc1fzr x1k90msu x6o7n8i xbxq160".split())
    wait = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
    time.sleep(uniform(1, 2))

    # faccio lo switch a all comments e clicco all comments
    CSS_SELECTOR = '.' + '.'.join("x6s0dn4 x78zum5 xdj266r x11i5rnm xat24cr x1mh8g0r xe0p6wg".split()) + " > div"
    button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
    wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button))
    button.click()
    time.sleep(uniform(1, 2))
    CSS_SELECTOR = '.' + '.'.join("x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h".split())
    all_comments = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR)))[2]
    all_comments.click()
    time.sleep(uniform(1, 2))

    # seleziono gli elementi view reply and more comments
    # view more replies
    "x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv x1mnrxsn"
    # see more
    "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"
    # view more comments
    "x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv"
    CSS_SELECTOR_1 = '.' + '.'.join("x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv x1mnrxsn".split())
    CSS_SELECTOR_2 = '.' + '.'.join("x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f".split())
    CSS_SELECTOR_2 = "div" + CSS_SELECTOR_2
    CSS_SELECTOR_3 = '.' + '.'.join("x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv".split())
    replies_more = driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR_1 + "," + CSS_SELECTOR_2 + "," + CSS_SELECTOR_3)

    def expand_everything(driver, buttons):
        count = 0
        for button in buttons:
            wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button))
            button.click()
            time.sleep(uniform(1, 2))
            count = count + 1
            new_buttons = driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR_1 + "," + CSS_SELECTOR_2 + "," + CSS_SELECTOR_3)
            if len(new_buttons) > len(buttons) - count:
                expand_everything(driver, new_buttons)
                break

    expand_everything(driver, replies_more)

    # adesso raccolgo tutti i commenti
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_comments = soup.find_all("div", {"class": "x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1pi30zi"})
    
    # metto i commenti in un csv
    output_file = "Facebook\csv_docs\comments.csv"
    with open(output_file, 'a', encoding='utf-8', newline='') as handle_w:
        csv_writer = csv.writer(handle_w, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        headers = ["comment_id", "post_id", "author", "content", "date", "time_of_fetching"]
        csv_writer.writerow(headers)

        i = 0
        for comment in all_comments:
            # estraggo l'autore
            try:
                CSS_SELECTOR = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u"
                author = comment.find("span", {"class": CSS_SELECTOR}).get_text()
            except:
                author = None
            # estraggo il contenuto
            try:
                CSS_SELECTOR = "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"
                content = comment.find("div", {"class": CSS_SELECTOR}).text
            except:
                content = None
            # estraggo la data
            try:
                CSS_SELECTOR = "html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"
                date = comment.find("span", {"class": CSS_SELECTOR}).get_text()
            except:
                date = None
            csv_writer.writerow([i, post_id, author, content, date, datetime.now()])
            i = i + 1

    