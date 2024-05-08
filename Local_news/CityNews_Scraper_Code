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
import xml.dom.minidom
from datetime import datetime
import locale

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)

#target_url = 'https://www.agrigentonotizie.it/' #done
# target_url = 'https://www.anconatoday.it/' #done
#target_url = 'https://www.arezzonotizie.it/' #done
# target_url = 'https://www.avellinotoday.it/' #done
#target_url = 'https://www.baritoday.it/' #done
#target_url='https://www.bolognatoday.it/' #done
#target_url = 'https://www.bresciatoday.it/'#done
#target_url = 'https://www.brindisireport.it/' # done
#target_url = 'https://www.casertanews.it/'#done
#target_url = 'https://www.cataniatoday.it/'#done - NO RESULTS
#target_url = 'https://www.cesenatoday.it/' #done
#target_url = 'https://www.chietitoday.it/' #done
#target_url = 'https://www.ferraratoday.it/' #done
#target_url = 'https://www.firenzetoday.it/' #solo un articolo
#target_url = 'https://www.foggiatoday.it/' #done
#target_url = 'https://www.forlitoday.it/' #done
#target_url = 'https://www.frosinonetoday.it/' #done
#target_url = 'https://www.genovatoday.it/' #done
#target_url = 'https://www.ilpescara.it/' #done
#target_url = 'https://www.ilpiacenza.it/' #done
#target_url = 'https://www.latinatoday.it/' #done
#target_url = 'https://www.lecceprima.it/' #done
#target_url = 'https://www.leccotoday.it/' #done - NO RESULTS
#target_url = 'https://www.livornotoday.it/' #solo un articolo
#target_url = 'https://www.messinatoday.it/' #done
#target_url = 'https://www.milanotoday.it/' #done
#target_url = 'https://www.modenatoday.it/' #done
#target_url = 'https://www.monzatoday.it/' #done
#target_url = 'https://www.napolitoday.it/' #done
#target_url = 'https://www.novaratoday.it/' #done
#target_url = 'https://www.perugiatoday.it/' #done
#target_url = 'https://www.pisatoday.it/' #done
#target_url = 'https://www.padovaoggi.it/' #done
#target_url = 'https://www.palermotoday.it/' #done
#target_url = 'https://www.parmatoday.it/' #done
#target_url = 'https://www.pordenonetoday.it/' #done
#target_url = 'https://www.quicomo.it/' #solo un risultato
#target_url = 'https://www.ravennatoday.it/' #done
#target_url = 'https://www.reggiotoday.it/' #done
#target_url = 'https://www.riminitoday.it/' #done
#target_url = 'https://www.romatoday.it'  #done
#target_url = 'https://www.salernotoday.it/'  #done
#target_url = 'https://www.sondriotoday.it/' #done
#target_url = 'https://www.ternitoday.it/' #done
#target_url = 'https://www.torinotoday.it/' #done
#target_url = 'https://www.trentotoday.it/' #done
#target_url = 'https://www.trevisotoday.it/' #done
#target_url = 'https://www.triesteprima.it/' #done
#target_url = 'https://www.udinetoday.it/'  #done
#target_url = 'https://www.veneziatoday.it/' #done
#target_url = 'https://www.veronasera.it/' #done
#target_url = 'https://www.vicenzatoday.it/' #NO REUSLTS
target_url = 'https://www.viterbotoday.it/' #done




driver.get(target_url)

query = 'agricoltori trattori'

wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button')))
print('Cookie element located')
cookie_button = driver.find_element(By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button')
time.sleep(5)
cookie_button.click()
print('Cookies accepted')

search_element = driver.find_element(By.XPATH, '//*[@id="c-header"]/div[1]/div[1]/div[3]/div[2]')

search_element.click()
print('Search bar opened')
search_bar = driver.find_element(By.XPATH, '//*[@id="c-header"]/div[2]/div/form/input')
search_bar.send_keys(query)
print('Query sent')
enter_button = driver.find_element(By.XPATH, '//*[@id="c-header"]/div[2]/div/form/button')
time.sleep(5)
enter_button.click()
print('Button clicked')

driver.switch_to.window(driver.window_handles[0])
time.sleep(15)

#print(result_list)

results = []
visited_urls = []

while True:
    # Find all title elements on the current page
    result_list = driver.find_elements(By.CSS_SELECTOR, '.c-story__header a.o-link-text[href]')

    # Extract title text and href attributes and append to results
    results += [(title_element.text, title_element.get_attribute('href')) for title_element in result_list]

    current_url = driver.current_url
    #print(current_url)
    if current_url in visited_urls:
        print("Reached the last page. Exiting the loop.")
        break
    else:
        visited_urls.append(current_url)

    try:
        # Find and click the 'next page' button
        next_page_button = driver.find_element(By.CSS_SELECTOR, '.c-pagination__item.c-pagination__item--arrow.u-flex.u-items-center.u-justify-center.u-mr-base')
        driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
        time.sleep(5)
        icon = driver.find_elements(By.CSS_SELECTOR, '.c-pagination__item.c-pagination__item--arrow.u-flex.u-items-center.u-justify-center.u-mr-base')
        icon[-1].click()

        # Wait for the new page to load by waiting for staleness of the first title element
        WebDriverWait(driver, 10).until(EC.staleness_of(result_list[0]))

    except Exception as e:
        # Print exception and break out of the loop
        print("Error occurred while scraping:", str(e))
        break

# Once finished, print or process the results

#print('Here are the results:', results)

locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

date_threshold = datetime(2023, 10, 1)

for result, result_url in results:
    try:
        driver.get(result_url)
        print('Fetching article:', result)

        wait = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'l-entry__title')))
        time.sleep(10)

        print('Element found')

        date_element = driver.find_element(By.CSS_SELECTOR, 'span.u-label-08[data-timestamp]')
        article_date = datetime.strptime(date_element.text, '%d %B %Y %H:%M')

        if article_date < date_threshold:
            continue

        journalist = driver.find_element(By.CSS_SELECTOR, 'span.u-label-05.u-mb-xxsmall.u-block')
        print('Jounalist\'s name found')
        edition = driver.find_element(By.CSS_SELECTOR, '[data-edition]')
        print('Edition found')
        date = driver.find_element(By.CSS_SELECTOR, 'span.u-label-08[data-timestamp]')
        print('Date found')
        title = driver.find_element(By.CLASS_NAME, 'l-entry__title')
        print('Title found')
        subtitle = driver.find_element(By.CLASS_NAME, 'l-entry__summary')
        print('Subtitle found')
        paragraphs = driver.find_elements(By.CSS_SELECTOR, 'div.c-entry p')
        p_texts = [p.text.strip() for p in paragraphs]
        print('Text found')


        with open(result + '.csv', "w", encoding="utf-8") as handle:
            file_writer = csv.writer(handle, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            file_writer.writerow(["Autore", "Data", "Edizione", "Titolo", "Sottotitolo", "Testo"])
            file_writer.writerow([journalist.text, date.text, edition.get_attribute('data-edition'), title.text, subtitle.text, p_texts])
            print('csv Created')


    except Exception as e:
        print("Error:", str(e))


time.sleep(30)

driver.quit()



