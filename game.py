import readchar as rc
import random
import time
import hashlib

# To remove the high scores file,
# search for the .scores file.
# It is hidden as denoted with
# the dot at the start.  

def saving_highscore(score):
    try:
        file = open(".scores", "r")
    except FileNotFoundError:
        file = file = open(".scores", "w+")

    try:
        if int(file.read()) < score:
            print("\nNew Highscore!")
            file = open(".scores", "w")
            file.write(str(score) + "\n" + str(hashlib.sha256(str(score).encode()).hexdigest()))
    except ValueError:
        usrInput = input("Create new .scores file? Will delete file in directory named that (Y/n)")
        if usrInput == "" or "Y" or "y":
            file = open(".scores", "w")
            file.write(str(score) + "\n" + str(hashlib.sha256(str(score).encode()).hexdigest()))
        elif usrInput == "n" or "N":
            print("File not created")
        else:
            file = open(".scores", "w")
            file.write(str(score) + "\n" + str(hashlib.sha256(str(score).encode()).hexdigest()))
    file.close()
    exit()

## Commands can be remapped to user's liking
LEFT = 'a'
RIGHT = 'd'
UP = 'w'
DOWN = 's'

keyInput = 0
seed = []
choice = [UP, DOWN, LEFT, RIGHT]
score = 0

## High score managing
try:
    file = open(".scores", "r")
    high_score, hash = file.read().split()
    if hash != hashlib.sha256(str(high_score).encode()).hexdigest(): # basic anti-cheat
        print("This .scores file is not valid. Don't cheat")
        exit()
except (ValueError, FileNotFoundError):
    high_score = "0"

while (keyInput != 'q'):
    print("\033[2J\033[;H", end='') # clear the screen
    seed.append(random.choice(choice)) # add random letter

    print(" ".join(seed))
    time.sleep(score/2+0.5) # amount of time is determined by length
    print("\033[2J\033[;H", end='') # clear the screen
    
    print("Highscore = " + high_score)
    print(u"\u001b[1000D") # send cursor to left
    print("Score = " + str(score))
    score += 1
    for i, val in enumerate(seed):
        keyInput = rc.readkey()
        if keyInput != val:
            space = i * 2 if i > 0 else 1
            print(u"\u001b[1000D") # send cursor to left
            print("\nwromg")
            print(u"\u001b[1000D") # send cursor to left
            print(" ".join(seed[:i]) + u" \u001b[41;1m" + keyInput + u"\u001b[0m " + " ".join(seed[i+1:]))
            print(u"\u001b[1000D") # send cursor to left
            print(" " * space + u"\u001b[32;1m" + seed[i] + u"\u001b[0m")
            saving_highscore(score)