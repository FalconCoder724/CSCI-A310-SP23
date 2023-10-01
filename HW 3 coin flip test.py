import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coins = []
    for i in range(100):
        if random.randint(0,1) == 0:
            coins += 'H'
        else: 
            coins += 'T'
        coins = " ".join(coins)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if "H" * 6 in coins or "T" * 6 in coins:
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
