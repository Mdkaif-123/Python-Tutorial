
# ? request module is used to create the request to he APIs

# * Request can be GET,POST,PUT,PATCH

import requests

    #* BeatifulSoup is used for web scraping 

from bs4 import BeautifulSoup

response = requests.get('https://google.com')

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())        #* To get all html in beautiful format 
# print(soup.title)             #* To get all the title in the response
# print(soup.title.string)      #* To get the title string

#* Abstracting all the links from the response 

list_of_links = []
for link in soup.find_all('a'):
    list_of_links.append(link.get('href'))
    
print(list_of_links)
