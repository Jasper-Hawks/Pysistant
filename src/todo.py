import platform
import os

# Figure out which os we are on 

def setup(): # Sets up the directory and many other dependencies needed for the program to function
    comp = platform.system()
    if comp == "Windows": # Check if we are on Windows and warn the user
        print("Pysistant does not officially support your OS but you are still allowed to try and setup the TODO list.\nIf you have any issues please open an issue on Github.")
        dir = input("In what directory would you like your TODO list to be stored?\n")
    else: 
        dir = input("In what directory would you like your TODO list to be stored? (Please make sure the last directory ends with a /)\n")
    try: 
        os.mkdir(dir + "TODO/TODO.txt")
    except PermissionError:
        print("Invalid input")


def read(): # Function to read the file
    pass

def write(): # Function to write to the file
    pass

if __name__ == "__main__":
    #TODO Change this eventually
    setup()