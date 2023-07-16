from ATMsystem.system import ATMsystem
import sys


def test(system: ATMsystem, cardNumber, pin, account, action, money=0):
    # print("    input:", cardNumber, pin, account, action, money)
    try:
        myATMsystem.readCard(str(cardNumber))
        myATMsystem.checkPinCorrect(str(pin))
        accountNums = myATMsystem.getAccountNums()
        myATMsystem.selectAccount(str(accountNums[account-1]))

        if(action == 1):
            balance = myATMsystem.getBalance()
            print("See Balance:", balance)
        elif(action == 2):
            if(myATMsystem.deposit(money)):
                print("Deposit Success")
        elif(action == 3):
            if(myATMsystem.withdraw(money)):
                print("Withdraw Success")
        return True
    
    except Exception as e:
        print(e)
        return False


        
if __name__ == '__main__':
    file_path = "testcase.txt"
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        
    with open(file_path, 'r') as f:
        N = f.readline()
        
        myATMsystem = ATMsystem()

        success = 0

        for i in range(int(N)):
            print('\n-------------',i,'-------------\n')
            line = f.readline()
            case = eval(line)
            if(test(myATMsystem, *case)):
                print("test case:", i, " => Success!")
                success += 1
            else:
                print("test case:", i, " => Fail!")

        print('\n---------TEST RESULT---------\n')
        print("  Success:", success, "Fail:", int(N)-success)

