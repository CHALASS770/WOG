from Utils import *

class Scores :
    def __init__(self ,nameP, play, difficult) :
        self.score = 0
        self.diffic = difficult
        self.namep = nameP
        self.Play = play
        self.newscore = 0
    def Write_Score(self):
        self.score = self.diffic * 3 + 5
        self.score = str(self.score)
        self.newscore = Utils(self.namep, self.Play, self.score)
        self.newscore.write_score()

    def read(self):
        self.newscore.read_score()
