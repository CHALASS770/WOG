from live import *
from Scores import *
from MainScore import *
name = input("whats your name ?")
welcome(name)

while True:
    play, level = load_game()
    play_game(play,level)
    Score = Scores(name, play ,level)
    Score.Write_Score()
    want=input('do you want play again ? y/n')
    if want == 'n' :
        break

