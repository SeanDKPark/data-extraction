import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = webdriver.ChromeOptions()

'''
selenium 4.0부터 아래 방식 사용
1. ChromeDriverManager().install() installs chromedriver and returns path
2. ChromeService() takes the installed path as input and manages the driver
3. webdriver.Chrome initializes chrome webdriver with service input
For more on initialization of the driver, check
https://pypi.org/project/webdriver-manager/
'''
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.set_window_size(1920, 1080)

#RP매각
url_sell = 'https://www.bok.or.kr/portal/singl/newsData/list.do?pageIndex=1&targetDepth=&menuNo=201150&syncMenuChekKey=9&depthSubMain=&subMainAt=&searchCnd=2&searchKwd=RP%EB%A7%A4%EA%B0%81&date=&sdate=&edate=&sort=1&pageUnit=10'

url = 'https://www.bok.or.kr/portal/main/main.do'

def collect_urls_and_titles():
    result_elements = driver.find_elements(By.CSS_SELECTOR, '#bbsList > div.bd-line > ul > li')
    filtered_urls = []
    titles = []
    for result_element in result_elements:
        title_element = result_element.find_element(By.CSS_SELECTOR, 'div > a')
        if 'RP매각' in title_element.text and '결과' in title_element.text:
            post_url = title_element.get_attribute('href')
            filtered_urls.append(post_url)
            titles.append(title_element.text)
    return filtered_urls, titles

def click_next_and_wait(cur_page):
    next_button = driver.find_element(By.CSS_SELECTOR,
                                      '#bbsList > div.paginationSet > div > ul > li:nth-child({}) > a > span'.format(cur_page+1+2))
    next_button.click()
    # element_locator = (By.CSS_SELECTOR, '#bbsList > div.paginationSet > div > ul > li:nth-child({})'.format(cur_page+1+2))
    # wait.until(active_class_of_nth_child(element_locator))
    time.sleep(1)

def click_next_10():
    next_button = driver.find_element(By.CSS_SELECTOR,
                                      '#bbsList > div.paginationSet > div > ul > li.i.next')
    next_button.click()
    time.sleep(1)

driver.get(url)

driver.implicitly_wait(10)
time.sleep(1)

news = driver.find_element(By.CSS_SELECTOR, '#gnb > ul > li.menu03 > a > span')
news.click()
driver.implicitly_wait(10)
time.sleep(1)

search = driver.find_element(By.CSS_SELECTOR, '#frm > div.sh-db > div.db-search > div.search-box > span > input[type=text]')
search_query = 'RP매각'
search.send_keys(search_query)
search.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
time.sleep(1)

dropdown = driver.find_element(By.ID, 'pageUnit')
drop = Select(dropdown)
drop.select_by_visible_text('100개')

# Setup wait for later
# wait = WebDriverWait(driver, 10)

driver.implicitly_wait(10)
time.sleep(1)

all_urls = []
all_titles = []

total_results = driver.find_element(By.CSS_SELECTOR,
                                        '#bbsList > div.sh-BxSet > p > strong')
num_total_results = int(total_results.text.replace(',', ''))
num_pages = (num_total_results + 100 - 1) // 100

for cur_page in range(1, num_pages+1):
    urls, titles = collect_urls_and_titles()
    all_urls.extend(urls)
    all_titles.extend(titles)
    print(len(all_urls))

    if cur_page == num_pages:
        print('done')
        break
    if cur_page % 10 != 0:
        click_next_and_wait(cur_page % 10)
    else:
        click_next_10()

data = []
for i in range(len(all_urls)):
    driver.get(all_urls[i])

    driver.implicitly_wait(10)

    element = driver.find_element(By.CSS_SELECTOR, '#board > div > div.dbdata')
    text = element.text
    data.append({'URL' : all_urls[i], 'Titles' : all_titles[i], 'Text' : text})

driver.quit()

df = pd.DataFrame(data)
print(df)

df.to_csv('rp_sell.csv', index = False)