""" Settings
This file will try to automate where the source comes from, so editing it should not be necessary, but for now it will be hard coded

function that will take user input, search for the book they want on google and do its best to find the story online.

"""
from bs4 import BeautifulSoup
import requests

#this class is the main file.
class NetReader:


    #constructor designed to load things like settings.source as usable variables on object creation.
    def __init__(self):
        #Booksites 
        Novel12 = "https://novel12.com/"
        Gutenberg = "https://www.gutenberg.org/"

        #source we're using
        source = Novel12

    #adds the users input search string to the end of the website and processes it through requests.
    # The return is a list of the results
    def search(self, website = "none"):

        bigstring = ""

        #url_input = input("Please enter your novel12 url here: ")
        # https://novel12.com/the-crystal-shard/4-the-crystal-shard-68738.htm
        r = requests.get("https://novel12.com/the-crystal-shard/4-the-crystal-shard-68738.htm")

        soup = BeautifulSoup(r.text, 'html.parser')

        # extracts out the <br></br> and all the content inside.

        for para in soup.find_all('p'):
            # print(para.get_text())
            bigstring += para.get_text() + '\n' + '\n'

        print(bigstring)
    #asks the user to select from the choices
    def selection(self, user_input):
        print("hello world")
    #goes forward one page
    def nextpage(self, user_input):
    #section for Novel12
        if source == Novel12:
        #search for last link with book title in it
            print("hello world")
    #incomplete section for gutenberg
        if source == Gutenberg:
        #something
            print("hello world")
    #find first sentance of the book
    def readerprep(self, bookSentanceArrayValue = "none"):
        #must also place whole page in navigable array with each section of the array being a sentance

        if source == Novel12:
            #search for largest <p></p> in return of findall
            print("hello world")
        #needs work
        if source == Gutenberg:
            #something
            print("hello world")
        # grabs sentance and places it in unique string
        for sentance in bookSentance:
            #grabs sentance and places it in unique string
            sentanceString = "Sentance"

        return sentanceString

    def readSentance(self, wordsGoHere = "none"):
        #take input of the sentance and then reads aloud
        #voiceThingy(wordsGoHere)
        print("hello world")
    #takes input of book in array of sentances
    def readBook(self, wholePreppedBookHere = "none"):
        for i in wholePreppedBookHere:
            self.readSentance(i)
            # pause reader and record i as a variable for user
            if userinput == "x":
                print("hello world")


    #optionally put down here
    def voiceread(self, wordsfrombook = "none"):
        #says the word from the book over the speakers
        print("hello world")

object1 = NetReader()

object1.search()
