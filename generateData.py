import random
import json
import sys

cardNum = ["123456789", "111111111", "111333555", "222444666", "050505050"]

file_path = sys.argv[1]
if len(sys.argv) == 2:
    with open(file_path, 'r') as f:
       cardNum = f.read().split()


cardDic = {}
accountDic = {}
for c in cardNum:
    accounts = random.sample(range(100000000, 999999999), 5)
    for a in accounts:
        accountDic[a] = {"balance": random.randint(1,1000000)*100}

    cardDic[c] = {"password": c[::-1], "accounts":list(set(accounts))}

print(cardDic)
print(accountDic)

with open('./bankSystem/data/card.json','w') as f:
  json.dump(cardDic, f, ensure_ascii=False, indent=4)

with open('./bankSystem/data/account.json','w') as f:
  json.dump(accountDic, f, ensure_ascii=False, indent=4)