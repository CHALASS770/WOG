
class Utils :
    def __init__(self, namePlayer, play ,myscore):
        self.score_file_name = ""
        self.bad_return_code = -1
        self.chance=5
        self.score=myscore
        self.nameplay = namePlayer

        if play == 1:
            self.play = "Memorygame"
        elif play == 2:
            self.play = "GuessGame"
        elif play == 3:
            self.play = "Roulette Game"
    '''def Screen_Cleaner():'''


    def write_score(self):
        self.score_file_name = open("score.txt", "w")
        self.score_file_name.write(self.score)
        self.score_file_name.close()

    def read_score(self):
        self.score_file_name = open("score.txt", "r")
        print(self.score_file_name.read())
        self.score_file_name.close()