import time
from random import *

Yresponses = ["yes","y","ye","yea","yeah"]

money = int(input("How much money do you want to have! \n"))

def Gamble():
    global money
    if money == 0:
        print("You are a disgrace")
    print("meow :3")
    gambleMoney = int(input("How much u want to gamble? \n"))
    if gambleMoney > money:
        print("You dont have that much")
        Gamble()

    print("are you ready!")
    time.sleep(3)
    Win = randint(0, 2)
    print(Win)
    if Win == 1:
        winnings = gambleMoney * 2
        print(f"You won {winnings}!")
        money += winnings
        print(f"Balance is now {money}")
        Gamble()
    else:
        print(f"you Lost")
        money -= gambleMoney
        print(f"Balance is now {money}")
        Gamble()

Gamble()