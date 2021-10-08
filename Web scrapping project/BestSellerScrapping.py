# -*- coding: utf-8 -*-
"""
Created on Sat May 22 08:44:17 2021

@author: OmarHesham
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
driver=webdriver.Chrome(r'E:\ITI_AI_Work\Data Prep\chromedriver_win32\chromedriver.exe')
driver.get("https://www.amazon.in/gp/bestsellers/books/")
 
for c in range(1,3):
    driver.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg={}".format(c))
    book=driver.find_elements_by_xpath("//a[@class='a-link-normal']/div[@class='p13n-sc-truncated']")
    price=driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")

# for i in book:
#     print (i.text)

# for j in price:
#     print (j.text)
    if c==1:
        with open('E:\ITI_AI_Work\Data Prep\Assignments\BestSellers.csv', mode='w',encoding='utf-8',newline='') as csv_file:
             csv_writer=csv.writer(csv_file)
             csv_writer.writerow(['Book Name', 'Book Price'])
             for k in range(0,len(book)):
                print("Book Name:",book[k].text)
                print("BookPrice:",price[k].text)
                csv_writer.writerow([book[k].text,price[k].text])
                
    else:
         with open('E:\ITI_AI_Work\Data Prep\Assignments\BestSellers.csv', mode='a',encoding='utf-8',newline='') as csv_file:
             csv_writer=csv.writer(csv_file)
             csv_writer.writerow(['Book Name', 'Book Price'])
             for k in range(0,len(book)):
                print("Book Name:",book[k].text)
                print("BookPrice:",price[k].text)
                csv_writer.writerow([book[k].text,price[k].text])
                
        
        
   


    
    
time.sleep(2)
driver.close()