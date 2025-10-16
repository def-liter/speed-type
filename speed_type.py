import normal_dictionary
import easy_dictionary

import random
import time
from colorama import Fore, Style, init

init()

easy_dictionary.easy
normal_dictionary.normal

def pick_mode():
    while True:
        try:
            pick = int(input("choose a mode - easy (1), normal (2), or quit (0): "))
            if pick == 1:
                return easy_dictionary.easy
            elif pick == 2:
                return normal_dictionary.normal
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
