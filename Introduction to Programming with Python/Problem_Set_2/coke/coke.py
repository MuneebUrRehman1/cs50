amount_due = 50
accepted_coins = [25,10,5]
while(True):
    print("Amount Due:", amount_due)
    inserted_coins = int(input("Insert Coins: "))
    if inserted_coins in accepted_coins :
        amount_due = amount_due - inserted_coins
        if(amount_due == 0):
            print("Change Owed: 0")
            break