# Author: Jasper Hawks

from calculate import calc
from define import define

def main():
    a = input(" c = calc, d = define: ")
    if a == "c" or a == "C":
         calc()
    elif a == "d" or a == "D":
        define()

if __name__ == "__main__":
    main()
