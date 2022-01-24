import random
coin = ["Head", "Tail"]
toss = random.choice(coin)

selection = input("Head or Tail \n").title()

if selection == toss:
    print("You Win :- " + toss)
else:
    print("You Loss :- " + toss)

