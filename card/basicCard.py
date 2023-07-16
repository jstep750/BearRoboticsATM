from bankSystem.basicBank import BasicBank

class BasicCard():
    def __init__(self, cardNum: str, userName: str, bankSystem: BasicBank):
        self.cardNum = cardNum
        self.userName = userName
        self.pinChecked = False
        self.__accountNums = []
        self.bankSystem = bankSystem


    def checkPin(self, pin: str) -> bool:
        try:
            self.pinChecked = self.bankSystem.checkPin(self.cardNum, pin)
            if(self.pinChecked):
                return True
            return False
        except:
            raise
    
    
    def getAccountNums(self) -> list:
        if(self.pinChecked == False):
            raise Exception("[CARD]: Check PIN First!")
        
        if(not self.__accountNums):
            try:
                self.__accountNums = self.bankSystem.getAccountNums(self.cardNum)
            except: 
                raise
        return self.__accountNums





