import platform
import re
import os

# Figure out which os we are on

def setup(): # Sets up the directory and many other dependencies needed for the program to function
    comp = platform.system() # First we figure out what os we are on
    if comp == "Linux": # If we are on Linux then we are officially supported
            # Prompt the user to input a directory
            dir = input("In what directory would you like your TODO list to be stored starting from root? (Please make sure the last directory ends with a /)\n")
    else: # Otherwise warn the user that they are not officially supported
        print("Pysistant does not officially support your OS but you are still allowed to try and setup the TODO list.")
        dir = input("In what directory would you like your TODO list to be stored?\n")

    try: # Make the directory and todo file
        os.makedirs(dir + "/TODO/") # Recursivley create directories
        dirFile = open("dir.txt","w") # Create the dir directory so that the variable persist
        dirFile.write(dir) # Write to the file the directory we were given
        dirFile.close() # Close the file
        os.chdir(dir + "/TODO/")
        todoFile = open("todo.txt","w")
        todoFile.close()
        print("Make sure to export this directory to PATH")
    except PermissionError: # If permission is denied
        print("Permission denied")
    except FileExistsError: # If the directory inputted is the same as the previous one
        print("The TODO directory and file already exist there")


def read(): # Function to read the file

    # This block of code is repeated in all functions
    try:
        dir = open("dir.txt", "r") # Open the dir file and read from it
    except:
        print("dir.txt does not exist. Remove TODO directory and file and run setup again")

    todoDir = dir.readline() # Read the first line
    todoDir = todoDir + "TODO/" # Append the TODO directory to the directory
    os.chdir(todoDir) # Go to that directory
    todo = open("todo.txt" ,"r") # Open the todo text file and read from it
    lines = todo.readlines() # Put all of the lines in the file into a list

    for i in lines: # Then print all of the lines to the terminal
        print(i)


def write(): # Function to write to the file

    # First we need to find the TODO file then write to it
    note = input("What would you like your note to be?\n")
    try:
        dir = open("dir.txt", "r") # Open the dir file and read from it
    except:
        print("dir.txt does not exist. Remove TODO directory and file and run setup again")
    todoDir = dir.readline()
    todoDir = todoDir + "TODO/"
    os.chdir(todoDir)
    todo = open("todo.txt" ,"r")
    # Get the length of the list and add one
    # so that the ints are not off
    numOfLines = len(todo.readlines()) + 1

    todo = open("todo.txt" ,"a") # Open the todo file and append to it
    todo.write(str(numOfLines)+ ": " + note + "\n") # Write to the file with the numOfLines being the number of the entry
    todo.close() # Close the file

def remove(): # Function to remove notes from TODO
    # We need to first handle lines and their numbers
    # Then completely remove the line from the file
    # This should be all that we need to do in this function

    try:
        dir = open("dir.txt", "r") # Open the dir file and read from it
    except:
        print("dir.txt does not exist. Remove TODO directory and file and run setup again")
    todoDir = dir.readline()
    todoDir = todoDir + "TODO/"
    os.chdir(todoDir)
    todo = open("todo.txt" ,"r")
    numOfLines = todo.readlines()

    line = input("Which line would you like to remove?")
    try:
        line = int(line) # Convert the input to an int
    except ValueError: # If they input something that is not an int
        print("Invalid input") # Print invalid input
        exit() # And exit

    for i in range(len(numOfLines)): # Go through the indexes of list items
        if i == line - 1: # If the current index is the same as the one the user inputted - 1 due to indexes starting at 0
            todo = open("todo.txt", "r") # Open the todo file and read from it
            todoLines = todo.readlines() # Read all of the lines and append them to a list
            del todoLines[line - 1] # Delete the item that the user wanted deleted
            todo = open("todo.txt", "w") # Open the todo file and write to it
            j = 0 # Variable to list the items
            for k in todoLines: # Go through all of the items in the todo lines list
                j += 1 # Increment the list variable
                conline = re.sub("^.", str(j),k) # Substitute the first number for the one in the list variable j
                todo.write(conline) # Then write to the file
            todo.close()
            break

