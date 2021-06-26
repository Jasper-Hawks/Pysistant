import platform
import os

# Figure out which os we are on 

def setup(): # Sets up the directory and many other dependencies needed for the program to function
    comp = platform.system()
    if comp == "Linux": # Check if we are on Windows and warn the user
            dir = input("In what directory would you like your TODO list to be stored starting from root? (Please make sure the last directory ends with a /)\n")
    else: 
        print("Pysistant does not officially support your OS but you are still allowed to try and setup the TODO list.")
        dir = input("In what directory would you like your TODO list to be stored?\n")
    
    try: 
        os.makedirs(dir + "/TODO/TODO.txt") # Recursivley create directories
        # with open ("dir.txt", "w") as dirFile:
        dirFile = open("dir.txt","w")
        dirFile.write(dir)
        dirFile.close()
    except PermissionError: # If permission is denied
        print("Permission denied")
    except FileExistsError: # If the directory inputted is the same as the previous one
        print("The TODO directory and file already exist there")


def read(): # Function to read the file
    cwd = os.getcwd()


def write(): # Function to write to the file

    # First we need to find the TODO file then write to it
    #TODO change the directory to dir.txt
    note = input("What would you like your note to be?\n")
    dir = open("dir.txt", "r")
    todoDir = dir.readline()
    todoDir = todoDir + "TODO/"
    os.chdir(todoDir)
    todo = open("todo.txt" ,"r")
    numOfLines = len(todo.readlines()) + 1

    # TODO Eventually we will have to consolidate the 
    # lines in order for them to update accordingly
    # but for now I'll use this method to see if it works
    todo = open("todo.txt" ,"a")
    todo.write(str(numOfLines)+ ": " + note + "\n")
    todo.close()

def remove(): # Function to remove notes from TODO
    # We need to first handle lines and their numbers
    # Then completely remove the line from the file
    # This should be all that we need to do in this function
    
    dir = open("dir.txt", "r")
    todoDir = dir.readline()
    todoDir = todoDir + "TODO/"
    os.chdir(todoDir)
    todo = open("todo.txt" ,"r")
    numOfLines = todo.readlines()

    line = input("Which line would you like to remove?")
    line = int(line)
    for i in range(len(numOfLines)):
        if i == line - 1:
            todo = open("todo.txt", "r")
            todoLines = todo.readlines()
            # Eventually we'll have to modify each item in the
            # list individually in order to consolidate the list
            del todoLines[line - 1]
            todo = open("todo.txt", "w")
            for k in todoLines:
                todo.write(k)
            break


if __name__ == "__main__":
    #TODO Change this eventually
    remove()
