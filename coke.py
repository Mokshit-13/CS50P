amount_due = 50
coins = [5, 10, 25]
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in coins:
        amount_due -= coin
    if coin == 50:
        continue

print(f'Change owed: {-amount_due}')



