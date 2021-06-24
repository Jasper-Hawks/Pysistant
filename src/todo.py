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
    dir = os.getcwd()


def write(): # Function to write to the file

    # First we need to find the TODO file then write to it
    #TODO change the directory to dir.txt
    note = input("What would you like your note to be?\n")
    dir = open("dir.txt", "r")
    todoDir = dir.readline()
    print(todoDir)
    todoDir = todoDir + "TODO/"
    os.chdir(todoDir)
    todo = open("TODO.txt" ,"w")
    todo.write(note)
    todo.close()

if __name__ == "__main__":
    #TODO Change this eventually
    write()