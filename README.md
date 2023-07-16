# BearRoboticsATM
Implementation of a simple ATM controller

## Generate Test DB
- insert list of card numbers
- correct pin : reversed card number
- 5 accounts per card are randomly generated
- balance are randomly assigned to each accounts
- run generation code
    ```
    python generateData.py cardnum.txt
    ```
- cardnum.txt
    ```
    123456789
    001010101
    247983470
    ```
- card.json
    ```json
        {
            "123456789": {
                "password": "987654321",
                "accounts": [
                    517440613,
                    391932626,
                    854583287,
                    911776028,
                    999852094
                ]
            },
            "001010101": {
            ...
        }
    ```
- account.json
    ```json
        {
            "391932626": {
                "balance": 8699500
            },
            "999852094": {
                "balance": 71133800
            },
            "517440613": {
                "balance": 50308000
            },
            "854583287": {
                "balance": 81944300
            },
            "911776028": {
                "balance": 67354500
            }
            ...
        }
    ```

## Test Case
- 1st row : number of test cases (N)
- next N rows : [card number, input PIN, selected account num(1~5), action(1:See Balance/2:Deposit/3:Withdraw), money(if action is 2 or 3)]
- example: test.txt
    ```
    3
    [123456789, 987654321, 2, 1]
    [123456789, 987654321, 3, 2, 10000]
    [123456789, 987654321, 5, 3, 20000]
    ```

## Run Test
```
python main.py testcase.txt
```