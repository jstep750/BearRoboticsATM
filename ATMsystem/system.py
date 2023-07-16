from card.basicCard import BasicCard
from account.basicAccount import BasicAccount
from bankSystem.basicBank import BasicBank
from ATMsystem.cashBin import CashBin

class ATMsystem():
    def __init__(self):
        self.cashBin = CashBin()
        self.tempCard = None
        self.currentCard = None
        self.currentAccount = None
        self.currentBank = BasicBank()


    def readCard(self, cardNum, userName=""):
        self.tempCard = BasicCard(cardNum, userName, self.currentBank)
    

    def checkPinCorrect(self, pin):
        if(self.tempCard):
            if(self.tempCard.checkPin(pin)):
                self.currentCard = self.tempCard
            else:
                raise Exception("[SYSTEM]: PIN incorrect!")
            return True
        else:
            raise Exception("[SYSTEM]: Insert Card!")


    def getAccountNums(self):
        if self.currentCard:
            try:
                accountNums = self.currentCard.getAccountNums()
            except:
                raise
            return accountNums
        else:
            raise Exception("[SYSTEM]: No Valid Card!")
        

    def selectAccount(self, accountNum):
        if self.currentCard:
            try:
                currentAccount = BasicAccount(accountNum, self.currentCard)
            except:
                raise
            self.currentAccount = currentAccount
        else:
            raise Exception("[SYSTEM]: No Valid Card!")


    
    def getBalance(self):
        if self.currentAccount:
            try:
                balance = self.currentAccount.getBalance()
            except:
                raise
            return balance
        else:
            print("[SYSTEM]: No Valid Account Selected!")



    def deposit(self, money):
        if(self.currentAccount):
            try:
                self.cashBin.putMoney(money)
                self.currentAccount.deposit(money)
            except:
                raise
            return True
        else:
            print("[SYSTEM]: No Valid Account Selected!")

    
    def withdraw(self, amount):
        if(self.currentAccount):
            try:
                self.currentAccount.withdraw(amount)
                money = self.cashBin.getMoney(amount)
            except:
                raise
            return money
        else:
            print("[SYSTEM]: No Valid Account Selected!")

        



