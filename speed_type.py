import random
import time
from colorama import Fore, Style, init

init()

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

def pick_mode():
    while True:
        try:
            pick = int(input("choose a mode - easy (1), normal (2), or quit (0): "))
            if pick == 1:
                return easy
            elif pick == 2:
                return normal
            elif pick == 0:
                print("bye")
                exit()
            else:
                print("please pick 1, 2, or 0.")
        except ValueError:
            print("invalid input. Please enter a number.")


while True:
    mode = pick_mode()
    word_pick = random.choice(mode)
    
    print(f"\ntype this: {Fore.YELLOW}{word_pick}{Style.RESET_ALL}")
    
    start_time = time.time()
    user_input = input("your input: ")
    end_time = time.time()
    
    elapsed = end_time - start_time

    if user_input == word_pick:
        print(f"{Fore.GREEN}correct{Style.RESET_ALL} you typed it in {Fore.BLUE}{elapsed:.2f}{Style.RESET_ALL} seconds.\n")
    else:
        print(f"{Fore.RED}incorrect{Style.RESET_ALL} you typed '{Fore.RED}{user_input}{Style.RESET_ALL}' instead of '{Fore.GREEN}{word_pick}{Style.RESET_ALL}'.")
        print(f"time taken: {Fore.BLUE}{elapsed:.2f}{Style.RESET_ALL} seconds.\n")
