from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from collections import defaultdict

columns = defaultdict(list)
links = []
i =1
with open('Surat Unique URL.csv',encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        # i += 1
        # links.append(row['URL DELHI CARS'])
        # if i == 801:
        #   break

        #for (k,v) in row.items():
            #columns[k].append(v)
            
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

#driver.close()
header = ['RTO', 'OBV Fair Value','OBV good value','OBV verygood value','OBV Excellent Value',
          'Health Score','URL']
# meader = ['qerew', 'ertwe', 'qerew', 'qsfgfs']
count = 0
with open('droomdata.csv', 'w', encoding='UTF8') as f:
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
#         div = soup.find('div', {
#                         'class': 'd-position-relative d-padding-20 d-padding-top-15 d-padding-bottom-0 listing-card'})
#         # brand = div.find(
#         #     'h1', {'class': 'd-font-weight-500 d-font-size-22 d-text-dark d-margin-top-0'})
#         # brand_data = div.find_all('div', {'class': 'd-font-size-12'})
#         # selling_price = div.find('div', {'class': 'd-font-size-22'})
    divli =soup.find('div', {'class': 'd-position-relative d-bg-white d-border-radius-5 d-box-shadow-default d-padding-15 min-height'})
if divli is not None:
        lis = divli.find_all(
            'li', {'class': 'd-display-inline-block d-padding-right-20 d-width-50'})                  
        
        rtodiv = soup.find('div', {
                           'class': 'd-position-relative d-bg-white d-border-radius-5 d-box-shadow-default d-padding-10'})
        if rtodiv is not None:
               rtoli = rtodiv.find_all('li', {
                                'class': 'd-display-table-cell text-center d-padding-top-10 d-padding-bottom-10 d-valign-top d-padding-left-5 d-padding-right-5'})

fair=soup.find('div',{'id':'obv_fair'})
good = soup.find('div', {'id': 'obv_good'})
verygood=soup.find('div',{'id':'obv_vgood'})
excellent=soup.find('div',{'id':'obv_excellent'})
        #orbdivfair=soup.find('div',{'id':'obv_fair'})
        # print(orbdivgood.text.strip())
        # if brand is not None:
        #     data.append(brand.text.strip())
        # if brand_data is not None:    
        #     data.append(brand_data[1].text.strip())
        # if selling_price is not None:  
        #     data.append(selling_price.text.strip())
if rtoli is not None: 
    data.append(rtoli[3].text.strip())      
if fair is not None:
    data.append(fair.text.strip())
if good is not None:
   data.append(good.text.strip())
if verygood is not None:
    data.append(verygood.text.strip())
if excellent is not None:
    data.append(excellent.text.strip())    
if lis[2] is not None:
    data.append(lis[2].text.strip())
    data.append(link)
    writer.writerow(data)
    driver.close()
        