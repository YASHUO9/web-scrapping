# -*- coding: utf-8 -*-
"""

Created by :Yash
 
"""

from bs4 import BeautifulSoup

import lxml

import requests

url  = "https://webscraper.io/test-sites/e-commerce/allinone"


site = requests.get(url)
#print(site.text)
#in above we have got the html as a string

soup = BeautifulSoup(site.text,'lxml')
#print(soup)
#we have converted the string to html in the python 



#print(soup.header)

#print(soup.div)



#Tags
soup.header
soup.div


#Navigable Strings
tag = soup.header.p
print(tag.string)


# Or 

print(soup.header.p.string)


#Attributes



tag = soup.header.a
tag
tag.attrs
#print(tag)


#here i have got the attributes now 
print(tag.attrs)
print('\n')
#now i am adding the new attribute
tag['new_attributes'] = "This is my new attributes for you !"

print(tag.attrs)






