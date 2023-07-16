class CashBin():
    def __init__(self):
        self.money = 100000000
        self.maximum = 100000000000

    def putMoney(self, money: int) -> bool:
        if(self.money + money <= self.maximum):
            self.money += money
            return True
        else:
            raise Exception("[CASHBIN] Maximum deposit exceeded!")
    
    def getMoney(self, amount: int) -> int:
        if(self.money >= amount):
            self.money -= amount
            return amount
        else:
            raise Exception("[CASHBIN] Not enough money left!")