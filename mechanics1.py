from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from collections import defaultdict

columns = defaultdict(list)
links = []
i =881
with open('carlinks.csv',encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        i += 1
        links.append(row['URL DELHI CARS'])
        if i == 981:
          break
        # for (k,v) in row.items():
        #     columns[k].append(v)
            

# print(columns)

# url = "https://droom.in/cars"
# driver = webdriver.Chrome(r"C:\Users\Hp\Desktop\gomechanics\chromedriver.exe")
# driver.get(url)
# time.sleep(5)

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# all_divs = soup.find_all(
#     'div', {'class': 'jss210 card-body'})

# links = []
# for div in all_divs:
#     aa = div.find('a', href=True)
#     links.append(aa['href'])


# print(len(links))

# driver.close()
 



header = ['Brand', 'Distance & km,Details',
          'price', 'RTO', 'OBV', 'Health Score']
meader = ['qerew', 'ertwe', 'qerew', 'qsfgfs']
count = 0
with open('droomdata1.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for link in links:
        count += 1
        driver = webdriver.Chrome(r"C:\Users\Hp\Desktop\gomechanics\chromedriver.exe")
        driver.get(link)
        driver.execute_script("window.scrollTo(0, 300)") 
        time.sleep(3)
        data = []
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find('div', {
                        'class': 'd-position-relative d-padding-20 d-padding-top-15 d-padding-bottom-0 listing-card'})
        brand = div.find(
            'h1', {'class': 'd-font-weight-500 d-font-size-22 d-text-dark d-margin-top-0'})
        brand_data = div.find_all('div', {'class': 'd-font-size-12'})
        selling_price = div.find('div', {'class': 'd-font-size-22'})
        divli = soup.find('div', {
                          'class': 'd-position-relative d-bg-white d-border-radius-5 d-box-shadow-default d-padding-15 min-height'})
        lis = divli.find_all(
            'li', {'class': 'd-display-inline-block d-padding-right-20 d-width-50'})
        rtodiv = soup.find('div', {
                           'class': 'd-position-relative d-bg-white d-border-radius-5 d-box-shadow-default d-padding-10'})
        rtoli = rtodiv.find_all('li', {
                                'class': 'd-display-table-cell text-center d-padding-top-10 d-padding-bottom-10 d-valign-top d-padding-left-5 d-padding-right-5'})
        orbdiv = soup.find('div', {'id': 'obv'})
        print(orbdiv)
        if brand is not None:
            data.append(brand.text.strip())
        if brand_data is not None:    
            data.append(brand_data[1].text.strip())
        if selling_price is not None:  
            data.append(selling_price.text.strip())
        if rtoli is not None: 
           data.append(rtoli[3].text.strip())
        if orbdiv is not None:
            data.append(orbdiv.text)
        if lis[2] is not None:
          data.append(lis[2].text.strip())
        writer.writerow(data)
        driver.close()
        