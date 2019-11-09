from random import *
class  GuessGame :

    def __init__(self):
        self.secretNumber = 1
        self.difficulty= -1
        self.chance=5

    def generat_number(self, difficulty):
        self.secretNumber = int(randint(0, difficulty*10))
        self.chance=self.chance+1-difficulty
    def get_secret_number(self):
        return self.secretNumber
    def guess_from_user(self):
        valideplay = True
        while valideplay == True:
            try:
                self.difficulty = int(input("enter a number"))
                valideplay = False
            except:
                print('please enter a numeric value')
    def guet_guess_from_user(self):
        return self.difficulty
    def compare_result(self):
        print('Good luck')
        while self.chance > 0 and self.get_secret_number() != self.guet_guess_from_user():
            print('you have ', self.chance, ' chance')
            self.guess_from_user()
            self.chance = self.chance - 1
        if self.get_secret_number()== self.guet_guess_from_user():
            print("you Win")
        elif self.chance == 0:
            print("you lost")
            print('the value was ', self.secretNumber)




