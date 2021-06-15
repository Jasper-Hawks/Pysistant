# Author: Jasper Hawks

import requests # Import requests so that we can view HTML
import re # Import regex as I assume that we will need it later
from bs4 import BeautifulSoup # Parse HTML from requests through Beautiful Soup
from calculate import calc

def define(): # Dictionary function

    # Plan: 
    # We first need to find a website that hast
    # html that we can scrape without having to
    # use more regex than we need to. This is
    # going to be the main challenge since the 
    # majority of Dictionary websites are bloated
    # and don't seem to have any rhyme or reason
    # to their html. 

    # Problems:
    # Never finding a good website to scrape.
    # 
    # Regex being too complex to filter the 
    # html in a way that gives us just the
    # definitions

    # I've started work on the define function 
    # but need to find another website so I'm
    # putting this one on the back burner.
    dict = requests.get("https://www.online-utility.org/english/dictionary.jsp?word=fried")
    html = dict.text

    soup = BeautifulSoup(html, 'html.parser')

# This will be replaced later with cli
# arguments and all but for now this will
# fufil our needs


def main():
    a = input(" c = calc, d = define: ")
    if a == "c" or a == "C":
         calc()

if __name__ == "__main__":
    main()
