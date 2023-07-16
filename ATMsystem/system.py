from card.basicCard import BasicCard
from account.basicAccount import BasicAccount
from ATMsystem.cashBin import CashBin

class ATMsystem():
    def __init__(self):
        self.cashBin = CashBin()
        self.tempCard = None
        self.currentCard = None
        self.currentAccount = None


    def readCard(self, userName, cardNum):
        self.tempCard = BasicCard(userName, cardNum)
    

    def checkPinCorrect(self, pin):
        if(self.tempCard):
            if(self.tempCard.checkPin(pin)):
                self.currentCard = self.tempCard
                return True
            else:
                raise Exception("[SYSTEM]: PIN incorrect!")
        else:
            raise Exception("[SYSTEM]: Insert Card!")


    def getAccountNums(self):
        if self.currentCard:
            try:
                return self.currentCard.getAccountNums()
            except Exception as e:
                print(e)
        else:
            raise Exception("[SYSTEM]: No Valid Card!")
        

    def selectAccount(self, accountNum):
        if self.currentCard:
            try:
                self.currentAccount = BasicAccount(accountNum, self.currentCard)
            except Exception as e:
                print(e)
        else:
            raise Exception("[SYSTEM]: No Valid Card!")


    
    def getBalance(self):
        if self.currentAccount:
            try:
                return self.currentAccount.getBalance()
            except Exception as e:
                print(e)
        else:
            print("[SYSTEM]: No Valid Account Selected!")



    def deposit(self, money):
        if(self.currentAccount):
            try:
                self.cashBin.putMoney(money)
                self.currentAccount.deposit(money)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            print("[SYSTEM]: No Valid Account Selected!")

    
    def withdraw(self, amount):
        if(self.currentAccount):
            try:
                money = self.cashBin.getMoney(amount)
                self.currentAccount.withdraw(amount)
                return money
            except Exception as e:
                print(e)
                return False
        else:
            print("[SYSTEM]: No Valid Account Selected!")

        



