# Author: Jasper Hawks

import requests # Import requests so that we can view HTML
import re # Import regex as I assume that we will need it later
from bs4 import BeautifulSoup # Parse HTML from requests through Beautiful Soup

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

def calc(): # Calculator function


    # Plan:
    # We first separate every character in the equation
    # in an array. Then check the entire array for 
    # parenthesis. If we have none we evaluate from left
    # to right. If we do we evaluate the equation inside
    # the rightmost parenthesis then continue until we can
    # evaluate without having to worry about parenthesis.

    # Problems:
    # Solving more complex equations that 
    # are inside more parenthesis (specifically
    # those that have more than 2 operands.
    #
    # Operators that are on the outside of parenthesis
    # For Example (2 + 2)* 2
    eq = input("Submit your equation: ")
    eq = list(eq)
    ops = []
    for i in range(len(eq)):
         if eq[i] != " ":
             ops.append(eq[i])

    
    print(ops)

    

calc()
