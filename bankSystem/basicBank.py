import json

class BasicBank():
    def __init__(self):
        self.bankName = "BasicBank"
        self.bankInfo = "Basic Bank for Testing ATM system"
        with open('./bankSystem/data/card.json') as f:
            self.cardInfo = json.load(f)
        with open('./bankSystem/data/account.json') as f:
            self.accountInfo = json.load(f)
        
        
    def checkPin(self, userName, cardNum, pin):
        if cardNum in self.cardInfo:
            if(self.cardInfo[cardNum]["password"] == pin):
                return True
            return False
        else:
            raise Exception("[BANK] Invalid card number!")
    

    def getAccountNums(self, cardNum):
        if(cardNum in self.cardInfo):
            accountNums = self.cardInfo[cardNum]["accounts"]
            return accountNums
        else:
            raise Exception("[BANK] Invalid card number!")
    

    def getBalance(self, accountNum):
        if(accountNum in self.accountInfo):
            return self.accountInfo[accountNum]["balance"]
        else:
            raise Exception("[BANK] Invalid account number!")
    

    def deposit(self, accountNum, money):
        if(accountNum in self.accountInfo):
            self.accountInfo[accountNum]["balance"] += money
            return True
        else:
            raise Exception("[BANK] Invalid account number!")


    def withdraw(self, accountNum, amount):
        if(accountNum in self.accountInfo):
            if(self.accountInfo[accountNum]["balance"] >= amount):
                self.accountInfo[accountNum]["balance"] -= amount
                return amount
            else:
                raise Exception("[BANK] Not enough money in account!")
        else:
            raise Exception("[BANK] Invalid account number!")