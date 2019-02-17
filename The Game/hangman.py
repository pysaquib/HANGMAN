import string                                                 #Imports string module
import random                                                 #Imports random module
from words import choose_word                                 #Imports choose_word function from words.py module that returns a random secret word
from images import *                                          #Imports all functions from images.py module



def is_word_guessed(secret_word, letters_guessed):            #This function returns a True if the word is guessed else returns False
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    if(secret_word==guessed_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1

    return guessed_word
# print(get_guessed_word("kindness",["k","n","s","j","h"]))


def get_available_letters(all_letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    i = 0
    for i in all_letters_guessed:
        letters_left = letters_left.replace(i,'')
    return letters_left

def validInput(letter):
    if(len(letter)!=1 and letter!="hint"):
        return False
    if(letter.isalpha()!=True):
        return False
    return True

def getHint(secret_word,letters_guessed):
    hint = ""
    # secret_word_for_hint = secret_word
    for i in letters_guessed:
        secret_word = secret_word.replace(i,"")
    random_hint = (random.choice(secret_word))
    return random_hint


def hangman(secret_word):
    print ("Welcome to the game, Hangman!\n")
    print("Which difficulty mode do you want to play in?\nEnter *e* for *EASY* , *m* for *MEDIUM* , *h* for *HARD\n")
    level = input("ENTER YOUR CHOICE : ").lower()
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.\n")
    print ("You can ask for a hint letter once by typing 'hint'\n")
    if(level!='e' and level!='m' and level!='h'):
        print("You have entered wrong choice\nContinuing with EASY mode\n")
        level = 'e'

    letters_guessed = []
    every_letters_guessed = []
    i = 0
    flag = 0
    help = 0



    while(flag<len(IMAGES)-2):
        available_letters = get_available_letters(every_letters_guessed)
        print ("Available letters: " + available_letters)
        letter = input("Guess a letter : ").lower()

        if(validInput(letter)==False):
            print("INVALID INPUT\n")

        every_letters_guessed.append(letter)

        if(letter=="hint"):
            help+=1
            if(help==1):
                print("Your hint is : "+getHint(secret_word,letters_guessed))
            else:
                print("SORRY!! HINT IS AVAILABLE ONLY ONCE")

        if((letter in secret_word and validInput(letter) == True)):
            letters_guessed.append(letter)

            print("Good Guess !! "+get_guessed_word(secret_word,letters_guessed))
            print()
            if(flag!=0 and level == 'e'):
                print(IMAGES[flag])
                print("Remaining Lives : "+str((len(IMAGES)-2)-flag))
            if(flag!=0 and level == 'm'):
                print(IMAGES1[flag])
                print("Remaining Lives : "+str(((len(IMAGES1))-2)-flag))
            if(flag!=0 and level == 'h'):
                print(IMAGES2[flag])
                print("Remaining Lives : "+str(((len(IMAGES2))-2)-flag))

            if(is_word_guessed(secret_word,letters_guessed)==True):
                print(" * * Congratulations * * $$$ You won $$$")
                break
        elif(validInput(letter) == True and letter!="hint"):
            print("Sorry "+letter+" is not in secret_word\n")
            flag+=1
            if(level=='e'):
                print(IMAGES[flag])
                print("Remaining Lives : "+str(((len(IMAGES))-2)-flag))
            if(level=='m'):
                print(IMAGES1[flag])
                print("Remaining Lives : "+str(((len(IMAGES1))-2)-flag))
                if(flag>5):
                    print("You've run out of chances :( \n")
                    print("The word was : "+secret_word)
                    break
            if(level=='h'):
                print(IMAGES2[flag])
                print("Remaining Lives : "+str(((len(IMAGES2))-2)-flag))
                if(flag>3):
                    print("You've run out of chances :( \n")
                    print("The word was : "+secret_word)
                    break
            print(get_guessed_word(secret_word,letters_guessed))

    else:
        print("You've run out of chances :( \n")
        print("The word was : "+secret_word)


secret_word = choose_word()
hangman(secret_word)
