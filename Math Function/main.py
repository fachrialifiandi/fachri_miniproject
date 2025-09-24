import os
import math

os.system('cls')


def Menu(Choice):
    while True:
        print("\n      MAIN MENU")
        print('=====================')
        print('1. Faktorial')
        print('2. Fibonacci')
        print('3. Quadratic Equations')
        print('0. Out')
        Choice = int(input("What menu do you want to choose: "))

        if (Choice > 0) or (Choice < 3):
            return Choice
        else:
            print('Wrong number sir! ')
            os.system('pause')
            os.system('cls')


def faktorial():

    Number = int(input("What number do you want to factorize? "))

    if Number < 0:
        print('Factorial is not intended for negative numbers.')
    else:
        Result = 1
        if Number == 0:
            Result = 1
        else:
            for i in range(1, Number + 1):
                Result = Result * i

        print(f'Results of Factorials {Number} is {Result}')
        print()


def fibonacci():

    # Logikanya sederhana: setiap angka = jumlah dua angka sebelumnya.
    Number = int(input("What number do you want to put? "))

    if Number < 0:
        print('Negatif number is not allowed')

    a, b = 0, 1
    if Number == 1:
        print(f"Deret Fibonacci: {a}")
    else:
        for _ in range(Number):
            print(a, end=" ")

            a, b = b, a + b

        print()


def q_equations():

    a = int(input("What value of a? "))
    b = int(input("What value of b? "))
    c = int(input("What value of c? "))

    print(f"Equations: {a}x² + {b}x + {c} = 0")

    D = b**2 - 4*a*c
    if D < 0:

        print("\nThere is no real number")

    elif D == 0:
        x = -b / (2*a)

        print("\nTwin roots: {x}")

    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

        print(f"\nThe value is x1: {x1}, x2: {x2} ")


# Main Body
Choice = -1
while (Choice != 0):
    Choice = Menu(Choice)
    os.system('cls')

    match (Choice):
        case 1:
            faktorial()
        case 2:
            fibonacci()
        case 3:
            q_equations()
        case 0:
            print('Thanks for using this program.')

    os.system('pause')
    os.system('cls')
