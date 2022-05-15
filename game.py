import readchar as rc
import random
import time

def saving_highscore(score):
    try:
        file = open(".scores", "r")
    except FileExistsError:
        file = file = open(".scores", "w+")

    try:
        if int(file.read()) < score:
            print("\nNew Highscore!")
            file = open(".scores", "w")
            file.write(str(score))
    except ValueError:
        usrInput = input("Create new .scores file? Will delete file in directory named that (Y/n)")
        if usrInput == "" or "Y" or "y":
            file = open(".scores", "w")
            file.write(str(score))
        elif usrInput == "n" or "N":
            print("File not created")
        else:
            file = open(".scores", "w")
            file.write(str(score))
    file.close()
    exit()

LEFT = 'a'
RIGHT = 'd'
UP = 'w'
DOWN = 's'

keyInput = 0
seed = []
choice = [UP, DOWN, LEFT, RIGHT]
score = 0

try:
    file = open(".scores", "r")
    high_score = file.read()
except ValueError:
    pass

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
            file.close()
            saving_highscore(score)