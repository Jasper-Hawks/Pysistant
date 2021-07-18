import time

def timer(): # Function for the timer

    sec = 0 # Set seconds to 0
    try:
        minute = input("How many minutes would you like to time:") # Prompt the user to input a number of minutes
        minute = int(minute) # Convert the string to int
        while minute >= 0: # While minutes are not greater than or equal to 0
            while sec >= 0: # While seconds are greater or equal to 0
               if sec < 10: # If seconds are below 10
                   print(str(minute) + ":0" + str(sec), end="\r") # Print the time with an empty space to replace the 0
                   sec -= 1 # Subtract one second
                   time.sleep(1) # Wait one second
               else: # Otherwise
                   print(str(minute) + ":" + str(sec), end="\r") # Print the time without a space at the end
                   sec -= 1 # Subtract one second
                   time.sleep(1) # Wait one second
            # Once seconds are below 0
            sec = 59 # Make seconds equal to 59
            minute -= 1 # Subtract one minute
    except : # If the input is invalid print this
        print("Invalid input")

def stopwatch():
    # First we have to keep incrementing a second variable
    # until it reaches 59 then increment a minute variable
    # and reset the second variable back to 0
    sec = 0 # Initialize the second variable
    minute  = 0 # Initialize the minute variable
    while True: # We will always do this
        sec += 1 # Add one to the second
        if sec > 59: # If seconds are above 59
            minute += 1 # Add one to the minutes
            sec = 0 # Make seconds equal 0 again
        time.sleep(1) # Wait one second
        if sec < 10:
            print(str(minute) + ":0" + str(sec), end="\r")
        else:
            print(str(minute) + ":" + str(sec), end="\r")

if __name__ == "__main__":
    stopwatch()
