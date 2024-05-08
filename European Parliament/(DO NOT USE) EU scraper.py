from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

target_url = 'https://www.europarl.europa.eu/plenary/en/minutes.html'
query = 'green deal'

# opzioni per driver  che simulano comportamento umano
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)
# apro la pagina
driver.get(target_url)
time.sleep(5)

# gestione pop-up cookies 

cookie_popup = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookie-policy"]/div/div[2]/button[1]')))
cookie_button = driver.find_element(By.XPATH, '//*[@id="cookie-policy"]/div/div[2]/button[1]')
cookie_button.click()

# cerco la barra per la query
bar = driver.find_element(By.ID, 'criteriaSidesMiText')
# inserisco la query, seleziono il bottone di invio e clicco
search = bar.send_keys(query)
enter_button = driver.find_element(By.ID, 'sidesButtonSubmit')
enter_button.click()

# identifico i risultati della query
title_elements = driver.find_elements(By.CLASS_NAME, "title")

# itero su tittgli gli elementi
i = 0
for title_element in title_elements:
    # prova: trova il link per andare sulla pagina e clicca
    try:
        driver.switch_to.window( driver.window_handles[0])
        link = title_element.find_element(By.TAG_NAME, "a")
        link.click()
        print('Clicking on {}'.format(title_element.text))
    # aspetta che la pagina di carichi fino a che non si carica l'elemento che voglio trovare 'verbatim reports'
    # non riesco a trovare il selettore giusto - vedi nota sotto ***
        driver.switch_to.window(driver.window_handles[i+1])
        wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.switch_button_pv_cre a[href]'))
        )
    # trova l'elemento 'verbatim reports e clicca'
        time.sleep(5)       
        link2 = driver.find_element(By.CSS_SELECTOR, 'td.switch_button_pv_cre a[href]')
        print('Element was successfully found. Clicking on it...')
        link2.click()
    # except: se non  trovi l'elemento, dimmelo e continua
    except Exception as e:

        print("Error:", str(e))

    i = i + 1

time.sleep(600)



# *** Il CSS_SELECTOR dovrebbe essere td.switch_button_pv_cre ma mi dice che non lo trova. Ho provato anche con l'XPATH ma non funziona nemmeno quello
# (cosa che ha pure senso considerando che credo cambi di pagina in pagina). Ho anche provato con il By.LINK_TEXT ma nulla. 
# stong scienn pazzzz 

'''    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView();", link)
    # Click the link
    link.click()'''

''' * codice 2 * 

ADESSO SERVE SOLO AGGIUNGERE LA PARTE DI CODICE CHE PERMETTE DI SCORRERE IL LA LISTA '''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests

target_url = 'https://www.europarl.europa.eu/plenary/en/minutes.html'
query = 'green deal'

# opzioni per driver  che simulano comportamento umano
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)

# apro la pagina
driver.get(target_url)

# gestione pop-up cookies

cookie_popup = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookie-policy"]/div/div[2]/button[1]')))
time.sleep(5)
cookie_button = driver.find_element(By.XPATH, '//*[@id="cookie-policy"]/div/div[2]/button[1]')
cookie_button.click()

# cerco la barra per la query
bar = driver.find_element(By.ID, 'criteriaSidesMiText')
# inserisco la query, seleziono il bottone di invio e clicco
search = bar.send_keys(query)
enter_button = driver.find_element(By.ID, 'sidesButtonSubmit')
enter_button.click()

# identifico i risultati della query


title_elements = driver.find_elements(By.CLASS_NAME, "title a")

results = [(title_element.text, title_element.get_attribute('href')) for title_element in title_elements]

print('Accessing the for loop')

i = 0
# itero su tutti gli gli elementi
for report, report_url in results:
            # prova: trova il link per andare sulla pagina e clicca
    try:
        driver.get(report_url)
        print('Fetching report:', report)
            # aspetta che la pagina di carichi fino a che non si carica l'elemento che voglio trovare 'verbatim reports'
            # non riesco a trovare il selettore giusto - vedi nota sotto ***
        wait = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.switch_button_pv_cre a[href]'))
                )
            # trova l'elemento 'verbatim reports e clicca'
        new_page = driver.find_element(By.CSS_SELECTOR, 'td.switch_button_pv_cre a')

        print('Element was successfully found. Clicking on it...')

        xml_url = new_page.get_attribute('href')

        print('XML file located')

        xml_content = requests.get(xml_url).text

        filename = f"{report}.xml"  # You can customize the filename here
        with open(filename, "w", encoding="utf-8") as file:
            file.write(xml_content)
            print(f"XML document '{filename}' downloaded successfully.")

            # except: se non  trovi l'elemento, dimmi quale è il problema e continua
    except Exception as e:

        print("Error:", str(e))

    i += 1

driver.quit()
