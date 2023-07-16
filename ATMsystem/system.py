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
        self.bankSystem = BasicBank()


    def readCard(self, cardNum: str, userName: str = "") -> None:
        self.tempCard = BasicCard(cardNum, userName, self.bankSystem)
    

    def checkPinCorrect(self, pin: str) -> bool:
        if(self.tempCard):
            if(self.tempCard.checkPin(pin)):
                self.currentCard = self.tempCard
                return True
            else:
                raise Exception("[SYSTEM]: PIN incorrect!")
        else:
            raise Exception("[SYSTEM]: Insert Card!")


    def getAccountNums(self) -> list:
        if self.currentCard:
            return self.currentCard.getAccountNums()
        else:
            raise Exception("[SYSTEM]: No Valid Card!")
        

    def selectAccount(self, accountNum: str) -> bool:
        if self.currentCard:
            self.currentAccount = BasicAccount(accountNum, self.currentCard)
            return True
        else:
            raise Exception("[SYSTEM]: No Valid Card!")

    
    def getBalance(self) -> int:
        if self.currentAccount:
            return self.currentAccount.getBalance()
        else:
            raise Exception("[SYSTEM]: No Valid Account Selected!")



    def deposit(self, money: int) -> bool:
        if(self.currentAccount):
            self.cashBin.putMoney(money)
            self.currentAccount.deposit(money)
            return True
        else:
            raise Exception("[SYSTEM]: No Valid Account Selected!")

    
    def withdraw(self, amount: int) -> int:
        if(self.currentAccount):
            self.currentAccount.withdraw(amount)
            money = self.cashBin.getMoney(amount)
            return money
        else:
            raise Exception("[SYSTEM]: No Valid Account Selected!")

        



