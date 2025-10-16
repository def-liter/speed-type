import random
import time
from colorama import Fore, Style

from colorama import init
init()

o = 0

easy = [
    "apple", "river", "mountain", "computer", "sunshine", "ocean", "forest", "book", "music", 
    "dream", "garden", "star", "window", "freedom", "light", "journey", "fire", "smile", "clock", "river"
]

normal = [
    "i ate an apple",
    "the river flows fast",
    "we climbed the mountain",
    "she bought a new computer",
    "the sunshine felt warm",
    "waves crashed in the ocean",
    "the forest was quiet",
    "he read a book",
    "i love listening to music",
    "he had a strange dream",
    "they walked in the garden",
    "a star shone brightly",
    "she looked out the window",
    "they fought for freedom",
    "the light was bright",
    "our journey began today",
    "the fire kept us warm",
    "her smile was kind",
    "the clock struck noon",
    "the river is wide"
]

mode = None

def pk_modes():
    global mode, o
    pick_modes = int(input("easy mode=1 normal mode=2: "))
    if pick_modes == 1:
        mode = easy
        o += 1
    elif pick_modes == 2:
        mode = normal
        o += 1
    else:
        print("pick 1 2 or 3")
        pk_modes()

if o == 0:
    pk_modes()

word_pick = random.choice(mode)

st = time.time()
asd = input(f"input {word_pick}: ")
et = time.time()
elapsed = et - st

if asd == word_pick:
    print(f"you wrote {Fore.GREEN}{word_pick}{Style.RESET_ALL} in {Fore.BLUE}{elapsed:.2f}{Style.RESET_ALL} seconds")
else:
    print(f"you wrote the incorrect word in {Fore.RED}{elapsed:.2f}{Style.RESET_ALL} seconds")
    print(f"you wrote {Fore.RED}{asd}{Style.RESET_ALL} instead of {Fore.RED}{word_pick}{Style.RESET_ALL} in {Fore.BLUE}{elapsed:.2f}{Style.RESET_ALL} seconds")

pk_modes()