# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:45:47 2023

@author: DELL
"""

import requests
from bs4 import BeautifulSoup

sites = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

#Checking if it is working or not
print(sites)
#its 200 then right is 404 or 400 then not working  at all 

soup = BeautifulSoup(sites.text,'lxml')
#print(soup.header)




#Find Function:
#print(soup.find('header'))


soup.header.attrs

print(soup.find('div',{'class':'container test-site'}))