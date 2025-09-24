import random
import os


os.system('cls')
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():

    while True:

        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please Enter a valid number!")
        else:
            print("Please enter a valid number.")

    return amount




balance = deposit()
print(f"You Have Deposit ${balance}")
