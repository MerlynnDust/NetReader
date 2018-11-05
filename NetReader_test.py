from bs4 import BeautifulSoup
import requests

r = requests.get('https://novel12.com/the-crystal-shard/4-the-crystal-shard-68738.htm')

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

links = [a.get('href') for a in soup.find_all('a', href=True)]

print(links)

#reccomendation for structure

"""class Book:
  load(String name)
  random_paragraph() String

class Display:
  print_text(PrintableString text)
  clear()

diff_strings(left String, right String) (float percent_similar, PrintableString diff)"""


#original function intent

"""

function1
    #this function take user input of a book, and asks for verification of it with the full author,
    #once the user verifies, the function then returns the data within the book.

function2
    #this function takes the book and finds the first paragraph

function3
    #this function splits the rest of the book into paragraphs


function4
    #this function reads through a for loop, the main section of our "game".
for loop
    #iterate through each paragraph here, storing as variable
    function5(paragraph)
        #take the paragraph var and print it to the user for a certain amount of seconds based on the amount of words present.
    function6(paragraph)
        #clear the screen, ask the user to type out what they remember of the paragraph
    function7(input)
        #compare the paragraph to the user input, determine a percentage and print it out.
    if userinput(space):
        #pause game and print page number and title of book.

"""
