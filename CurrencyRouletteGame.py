from random import *
from time import sleep

class  CurrencyRouletteGame:
    def __init__(self, difficult):
        self.total_money = int(randint(5,1000))
        self.intermin = 0
        self.intermax = 0
        self.difficult = difficult
        self.useramount = 0

    def get_money_interval(self):
        self.intermin=self.total_money - (5 - self.difficult)
        self.intermax=self.total_money + (5 - self.difficult)

    def get_guess_from_user(self):
        print(self.total_money,' USD')
        self.useramount=int(input('enter a value in ILS'))

    def play(self):
        self.get_money_interval()
        self.get_guess_from_user()
        if self.intermin<self.useramount<self.intermax:
            print('you win')
        else:
            print('you lost')
            print(self.intermin,'< ',self.useramount,'< ',self.intermax)