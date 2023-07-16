from bankSystem.basicBank import BasicBank
from card.basicCard import BasicCard

class BasicAccount():
    def __init__(self, accountNum, card: BasicCard):
        if(not card.pinChecked):
            raise Exception("[ACCOUNT]: Check Card PIN!")
        self.accountNum = accountNum
        self.card = card
        self.bankSystem = BasicBank()


    def getBalance(self):
        return self.bankSystem.getBalance(self.accountNum)


    def deposit(self, money):
        self.bankSystem.deposit(self.accountNum, money)


    def withdraw(self, amount):
        money = self.bankSystem.withdraw(self.accountNum, amount)
        return money

    