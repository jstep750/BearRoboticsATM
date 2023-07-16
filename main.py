from ATMsystem.system import ATMsystem
import sys

if len(sys.argv) == 2:
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
       N = f.readline()
       for i in range(N):
           line = f.readline()
           print(line)


# myATMsystem = ATMsystem()

# myATMsystem.readCard("Hyejin", "123456789")

# pin = "987654321"
# print(myATMsystem.checkPinCorrect(pin))

# accountNums = myATMsystem.getAccountNums()
# print(accountNums)

# for a in accountNums:
#     myATMsystem.selectAccount(a)
#     balance = myATMsystem.getBalance()
#     print(a,":",balance)




