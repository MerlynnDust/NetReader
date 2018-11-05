from bs4 import BeautifulSoup
import requests
import time



bigstring = ""

print("Welcome to Netreader Beta!")
time.sleep(1)
print("Currently we support novel12 but will add support for Project Gutenberg soon.")
time.sleep(1)

#this is a test push

#ask user for input and requests grab the site.

url_input = input("Please enter your novel12 url here: ")
#https://novel12.com/the-crystal-shard/4-the-crystal-shard-68738.htm
r = requests.get(url_input)

soup = BeautifulSoup(r.text, 'html.parser')


#extracts out the <br></br> and all the content inside.

for para in soup.find_all('p'):
    #print(para.get_text())
    bigstring += para.get_text() + '\n' + '\n'

#text= soup.body.find_all('p')
#text = soup("p")[1]

print(bigstring)

#prints all the links on the page
