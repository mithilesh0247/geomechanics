from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
url ="https://www.cardekho.com/buy-used-cars+in+gurgaon"
driver = webdriver.Chrome(r"C:\Users\Hp\Desktop\gomechanics\chromedriver.exe")
driver.get(url)
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all(
    'div', {'class':'holder hover'})

links = []
for div in all_divs:
    aa = div.find('a', href=True)
    links.append('https://www.cardekho.com/'+aa['href'])
print(len(links))        
print(links)    
driver.close()
header = ['Year and Brand ', ' Distance in km', 'Fuel_Type', 'Type', 'Price']

with open('spinnyData.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
count=1
for link in links:
        count += 1
        driver = webdriver.Chrome(r"C:\Users\Hp\Desktop\gomechanics\chromedriver.exe")
        driver.get(link)
        driver.execute_script("window.scrollTo(0, 300)") 
        time.sleep(3)
        data = []
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        divs=soup.find_all('div',{'class':'paddingBorder clearfix'})
        print(divs)
        #data = []
        #model = div.find(
            #'div', {'class': 'styles__yearAndMakeAndModelSection'}).text
#         km = div.find('p', {'class': 'styles__otherInfoSection'}).text
#         price = div.find('div', {'class': 'styles__priceSection'}).text
#         data.append(model)
#         if km[8] == 'p':
#             if km[len(km) - 1] == 'c':
#                 data.append(km.replace('petrolautomatic', ''))
#             else:
#                 data.append(km.replace('petrolmanual', ''))
#             data.append('petrol')
#         else:
#             if km[len(km) - 1] == 'c':
#                 data.append(km.replace('dieselautomatic', ''))
#             else:
#                 data.append(km.replace('dieselmanual', ''))
#             data.append('diesel')
#         if km[len(km) - 1] == 'c':
#             data.append('automatic')
#         else:
#             data.append('manual')
#         data.append(price.replace('‚¹', ''))
#         writer.writerow(data)

