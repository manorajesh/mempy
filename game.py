import curses
from random import choice
from time import sleep
from hashlib import sha256

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
        if int(file.read().split()[0]) < score:
            print("\nNew Highscore!")
            file = open(".scores", "w")
            file.write(str(score) + "\n" + str(sha256(str(score).encode()).hexdigest()))
    except (ValueError, IndexError):
        usrInput = input("Create new .scores file? Will delete file in directory named that (Y/n) ")
        if usrInput == "" or "Y" or "y":
            file = open(".scores", "w")
            file.write(str(score) + "\n" + str(sha256(str(score).encode()).hexdigest()))
        elif usrInput == "n" or "N":
            print("File not created")
        else:
            file = open(".scores", "w")
            file.write(str(score) + "\n" + str(sha256(str(score).encode()).hexdigest()))
    file.close()
    curses.endwin()
    exit()

def game(isHardMode): 

    ## Commands can be remapped to user's liking
    LEFT = 'a'
    RIGHT = 'd'
    UP = 'w'
    DOWN = 's'

    keyInput = 0
    seed = []
    score = 0

    X_TOP = 0
    Y_TOP = 0

    ## High score managing
    try:
        file = open(".scores", "r")
        high_score, hash = file.read().split()
        if hash != sha256(str(high_score).encode()).hexdigest(): # basic anti-cheat
            print("This .scores file is not valid. Don't cheat\nDelete it and restart the game")
            exit()
    except (ValueError, FileNotFoundError):
        high_score = "0"

    # curses initialization
    window = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)

    X_TOP = (curses.COLS - 23) // 2 # center the game
    Y_TOP = (curses.LINES - 7) // 2 # center the game

    try:
        if isHardMode:
            charset = "qwertyuiopasdfghjklzxcvbnm[]\-=,./_+<>?:" # hard mode
        else:
            charset = [UP, DOWN, LEFT, RIGHT]

        # game loop
        while (keyInput != 'q'):
            window.erase()
            window.refresh()
            curses.noecho()
            curses.curs_set(0)

            window.addstr(0+Y_TOP, 0+X_TOP, "Highscore = " + high_score)
            window.addstr(1+Y_TOP, 0+X_TOP, "Score = " + str(score))
            window.refresh()
            
            seed.append(choice(charset)) # add random letter

            # print seed then clear it after timeout
            window.addstr(3+Y_TOP, 0+X_TOP, " ".join(seed))
            window.refresh()
            sleep(0.5 * 1.3**score) # amount of time is determined by length
            window.deleteln()
            window.refresh()

            curses.flushinp() # clear input buffer to prevent user from reading while typing
            score += 1
            for i, val in enumerate(seed):
                while not (32 < (keyInput := window.getch()) < 127): # wait for user input to be printable
                    pass

                if keyInput != ord(val):
                    space = i * 2
                    window.addstr(3+Y_TOP, 0+X_TOP, " ".join(seed[:i]))
                    window.addstr(3+Y_TOP, space+X_TOP, f'{chr(keyInput)}', curses.color_pair(2))
                    window.addstr(3+Y_TOP, space + 2 + X_TOP, " ".join(seed[i+1:]))
                    window.addstr(4+Y_TOP, space+X_TOP, val, curses.color_pair(3) | curses.A_BLINK)
                    window.addstr(6+Y_TOP, 0+X_TOP, "wromg", curses.color_pair(2))
                    window.refresh()

                    # quit game
                    while True:
                        window.addstr(8+Y_TOP, 0+X_TOP, "Press Space to continue")
                        window.refresh()
                        if window.getkey() == " ":
                            saving_highscore(score)
    except Exception as e:
        # for curses to reset the terminal
        curses.endwin()
        print(e)

if __name__ == "__main__":
    game(False)