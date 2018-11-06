""" Settings
This file will try to automate where the source comes from, so editing it should not be necessary, but for now it will be hard coded

function that will take user input, search for the book they want on google and do its best to find the story online.

"""

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
    def search(website):

    #asks the user to select from the choices
    def selection(user_input):

    #goes forward one page
    def nextpage(userinput):
    #section for Novel12
    if source = Novel12:
        #search for last link with book title in it

    #incomplete section for gutenberg
    if source = Gutenberg:
        #something

    #find first sentance of the book
    def readerprep(bookSentanceArrayValue):
        #must also place whole page in navigable array with each section of the array being a sentance

        if source = Novel12:
            #search for largest <p></p> in return of findall

        #needs work
        if source = Gutenberg:
            #something

        # grabs sentance and places it in unique string
        for sentance in bookSentance:
            #grabs sentance and places it in unique string
            sentanceString = "Sentance"

        return sentanceString

    def readSentance(wordsGoHere):
        #take input of the sentance and then reads aloud
        voiceThingy(wordsGoHere)

    #takes input of book in array of sentances
    def readBook(wholePreppedBookHere):
        for i in wholePreppedBookHere:
            readSentance(i)
            # pause reader and record i as a variable for user
            if userinput = "x"


    #optionally put down here
    def voiceread(wordsfrombook):
        #says the word from the book over the speakers


 