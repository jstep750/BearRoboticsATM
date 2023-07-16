from bankSystem.basicBank import BasicBank

class BasicCard():
    def __init__(self, cardNum, userName, bankSystem: BasicBank):
        self.cardNum = cardNum
        self.userName = userName
        self.pinChecked = False
        self.__accountNums = []
        self.bankSystem = bankSystem


    def checkPin(self, pin):
        self.pinChecked = self.bankSystem.checkPin(self.userName, self.cardNum, pin)
        if(self.pinChecked):
            return True
        return False
    
    
    def getAccountNums(self):
        if(self.pinChecked == False):
            raise Exception("[CARD]: Check PIN First!")
        
        if(not self.__accountNums):
            self.__accountNums = self.bankSystem.getAccountNums(self.cardNum)
        return self.__accountNums





