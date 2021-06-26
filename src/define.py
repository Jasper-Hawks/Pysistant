import requests # Import requests so that we can requests websites to scrape data from
from bs4 import BeautifulSoup # Import Beautiful Soup so we can find elements in the html we get from requests
import re # Import Regex so that we can replace certain parts of the definitions 

def define():
    word = input("What word would you like to define?:") # Prompt the user to enter something this will be removed at a later date

    r = requests.get("http://wordnetweb.princeton.edu/perl/webwn/webwn?o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&s=" + word).text
    # Request the html of the wordnet site

    soup = BeautifulSoup(r,'html.parser') # Create a soup so that we can scrape elements off of the site

    for results in soup.find_all('li'): # Find every <li> tag in the html

        defins = results.text # This just takes the li tags off of the ends of the text
        defins = re.sub("^...", "",defins) # Use regex to get rid of the S: in front of all of the definitions

        print(defins) # Print the definitions to the screen

if __name__ == "__main__":
    define()
