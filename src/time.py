import time
import os

def timer():
    sec = 0
    min = input("How many minutes would you like to time")
    min = int(min)
    while min >= 0:
        while sec >= 0:
            print(str(min) + ":" + str(sec), end="\r")
            sec -= 1
            time.sleep(1)
        sec = 59
        min -=1
    print("Done", end="\r")

if __name__ == "__main__":
    timer()
