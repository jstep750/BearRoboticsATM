from bankSystem.basicBank import BasicBank
from card.basicCard import BasicCard

class BasicAccount():
    def __init__(self, accountNum: str, card: BasicCard):
        if(not card.pinChecked):
            raise Exception("[ACCOUNT]: Check Card PIN!")
        self.accountNum = accountNum
        self.card = card
        self.bankSystem = card.bankSystem


    def getBalance(self) -> int:
        return self.bankSystem.getBalance(self.accountNum)


    def deposit(self, money: int) -> bool:
        return self.bankSystem.deposit(self.accountNum, money)
        

    def withdraw(self, amount: int) -> int:
        return self.bankSystem.withdraw(self.accountNum, amount)
    