from GuessGame import *
from time import sleep
from MemoryGame import *
from CurrencyRouletteGame import *
def welcome(name):
    print("Hello %s ! Welcome in World of Game!!! "% name)
    print("Here you can find many cool games to play ")

def load_game():
    valideplay = True
    while valideplay == True:
        try :
            play=int(input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n 2. Guess Game - guess a number and see if you chose like the computer \n 3. Weather Roulette - Guess the current temperature currently in Jerusalem \n"))
            if 1 <= play <= 3 :
                valideplay = False
            else:
                raise ValueError("your choice is invalide")

        except ValueError:
            print("****please enter a valid value ****** \n ********************* \n")

    validedif = True
    while validedif == True:
        try :
            difficult = int(input("choose a dificult betwin 1 and 5 \n "))
            if 1 <= difficult <=5 :
                validedif = False
            else :
                raise ValueError("your choice is invalide")
        except ValueError:
            print("****please enter a valid value**** \n ********************\n")

    if play == 1 :
        print("you choose to play to Memory Game")
    elif play == 2:
        print("you choose to play to Guess Game")
    elif play == 3:
        print("you choose to play to Weather Roulette")

    if difficult == 1 :
        print("difficult is easy")
    elif difficult == 2:
        print("difficult is easy plus")
    elif difficult  == 3:
        print("difficult is hard")
    elif difficult == 4:
        print("difficult is hard plus")
    elif difficult  == 5:
        print("difficult is very Hard")
    return play, difficult

def play_game(playGame, level):
    sleep(3)

    if playGame == 2:
        for i in range(20):
            print('')
        print('**************************************')
        print('***** WELCOME TO THE GUESS GAME ******')
        print('**************************************')
        for i in range(3):
            print('')
        game = GuessGame()
        game.generat_number(level)
        game.compare_result()
    elif playGame == 1:
        for i in range(20):
            print('')
        print('**************************************')
        print('***** WELCOME TO THE MEMORY GAME ******')
        print('**************************************')
        for i in range(3):
            print('')
        game = MemoryGame(level)
        game.play()
    elif playGame == 3:
        for i in range(20):
            print('')
        print('**************************************')
        print('***** WELCOME TO THE ROULETTE GAME ******')
        print('**************************************')
        for i in range(3):
            print('')
        game = CurrencyRouletteGame(level)
        game.play()