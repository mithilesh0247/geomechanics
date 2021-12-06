from bs4 import BeautifulSoup
import time
import csv
from csv import reader
from csv import writer

i =0
data = []
with open('MumbaiCarLinks.csv','r',encoding="utf8") as read:
    rr = reader(read)
    for row in rr:
        data.append(row)
        i += 1
        if i == 626:
            break

index = 0
with open('mumbai626droomdata.csv','r',encoding="utf8") as read,open('mumbai1to626data.csv','w',newline='',encoding="utf8") as write:
    csv_reader = reader(read)
    csv_writer = writer(write)
    
    for row in csv_reader:
        print(row)
        row.append(data[index])
        csv_writer.writerow(row)
        index += 1
        
print(index)
print('complete')
