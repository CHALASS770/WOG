from random import *
from time import sleep
class  MemoryGame :
    def __init__(self, difficult):
        self.my_sequence = []
        self.list_from_user = []
        self.difficulty = difficult*2
        #self.valid=0
    def generate_sequence(self):
        for lenght in range(self.difficulty):
            self.my_sequence.append(int(randint(0, 101)))
        print('the sequence is : ', self.my_sequence)
        sleep(0.7)
        for i in range(30):
            print('')

    def get_list_from_user(self):

        for lenght in range(self.difficulty):
            self.list_from_user.append(int(input('enter the value ')))

    def is_list_equal(self):
        valid=0
        for lenght in self.my_sequence:
            for list_user in self.list_from_user:
                if lenght == list_user:
                    valid = valid + 1




        if valid == self.difficulty:
            return True

        else:
            return False


    def play(self):
        self.generate_sequence()
        self.get_list_from_user()
        if self.is_list_equal()==True :
            print('you win')
        else:
            print('you lost')

