from ctypes.wintypes import WORD
from itertools import count
import random
from sys import displayhook
import time
from xml.etree.ElementInclude import LimitedRecursiveIncludeError


print("\nWelcome to the game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of luck!")

def main():
    global count
    global display
    global word 
    global already_guessed 
    global length 
    global play_game
    words_to_guess = ("january", "border", "image", "film", "promise", "kids", "kids", 
    "lungs", "rhyme", "damage", "plants")

    word = random.choice(words_to_guess)
    length = len(word) 
    count = 0
    display = '_' * length 
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game 
    play_game = input("Do you want to play again? y = yes n = no\n") 
    while play_game not in ("y", "n", "Y", "N"):
        play_game = input("Do you want to play again? y = yes n = no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("See ya later then")
        exit() 

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 5

    guess = input("This is the Hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            # print(" _____ \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n")
            print("Wrong guess. " + str(limit -count) + " guesses remaining")
        elif count == 2:
            time.sleep(1)
            # print(" _____ \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n")
            print("Wrong guess. " + str(limit -count) + " guesses remaining")
        elif count == 3:
            time.sleep(1)
            # print(" _____ \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n")
            print("Wrong guess. " + str(limit -count) + " guesses remaining")
        elif count == 4:
            time.sleep(1)
            # print(" _____ \n"
            #       " |    |\n"
            #       " |    |\n"
            #       " |    |\n"
            #       " |    |\n"
            #       " |     \n"
            #       " |     \n"
            #       " |     \n")
            print("Wrong guess. " + str(limit -count) + " guesses remaining")
        elif count == 5:
            # print(" _____ \n"
            #       " |    |\n"
            #       " |    |\n"
            #       " |    |\n"
            #       " |    o\n"
            #       " |   /|\ \n"
            #       " |   / \ \n"
            #       " |    \n")
            print("You failed\n")
            print("The word was:", already_guessed, word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly")
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()