import readchar as rc
import random
import time

LEFT = 'a'
RIGHT = 'd'
UP = 'w'
DOWN = 's'

keyInput = 0
seed = []
choice = [UP, DOWN, LEFT, RIGHT]
score = 0
while (keyInput != 'q'):
    print("\033[2J\033[;H", end='') # clear the screen
    seed.append(random.choice(choice))

    print(" ".join(seed))
    time.sleep(score/2+0.5)
    print("\033[2J\033[;H", end='') # clear the screen
    
    print("Score = " + str(score))
    score += 1
    for i, val in enumerate(seed):
        keyInput = rc.readkey()
        if keyInput != val:
            space = i * 2 if i > 0 else 1
            print(u"\u001b[1000D")
            print("\nwromg")
            print(u"\u001b[1000D")
            print(" ".join(seed[:i]) + u" \u001b[41;1m" + keyInput + u"\u001b[0m " + " ".join(seed[i+1:]))
            print(u"\u001b[1000D")
            print(" " * space + u"\u001b[32;1m" + seed[i] + u"\u001b[0m")
            exit()