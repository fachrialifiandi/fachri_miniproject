from rich import print
import os


def program_menu():

    while True:
        os.system('cls')
        print("Converter Program")
        print('================\n')
        print('1. Weight Converter. ')
        print('2. Temperature Converter. ')
        print('0. Out.')

        try:
            print('\n[#048ABF]Which one do you choose?[/] ', end="")
            Choice = int(input())
            if (Choice >= 0) and (Choice <= 2):
                return Choice

            else:
                print('\nYou choose wrong number, please press enter.')
                os.system('pause')
        except ValueError:
            print('\n[#C51F1A]Invalid input, please input a number.[/]')
            os.system('pause')


def weight():

    while True:

        os.system('cls')

        try:
            weight = print('[#048ABF]Enter your weight:[/] ', end="")
            weight = float(input())
        except ValueError:
            print('[#C51F1A]Please enter a Valid number.[/]')
            os.system('pause')
            continue

        unit = print('[#048ABF]Kilograms or Pounds? (K or L):[/] ', end="")
        unit = input()

        if unit == "K":
            weight = weight * 2.205
            unit = "Lbs."
            print(f"Your weight is : {round(weight, 1)} {unit}")
            os.system('pause')
            break

        elif unit == "L":
            weight = weight / 2.205
            unit = "Kgs."
            print(f"Your weight is : {round(weight, 1)} {unit}")
            os.system('pause')
            break

        else:
            print(f"[#C51F1A]{unit} was not valid[/].")
            os.system('pause')
            continue


def temperature():

    while True:
        os.system('cls')

        unit = print(
            "[#048ABF]Is this temperature in Celcius or Fahrenheit (C/F):[/] ", end="")
        unit = input()

        try:
            temp = print("[#048ABF]Enter the temprature:[/] ", end="")
            temp = float(input())

        except ValueError:
            print('[#C51F1A]Please enter a Valid number.[/]')
            os.system('pause')
            continue

        if unit == "C":
            temp = round((9 * temp) / 5 + 32, 1)
            print(f'The temperature in Fahrenheit is : {temp}°F')
            os.system('pause')
            break

        elif unit == "F":
            temp = round((temp - 32) * 5/9, 1)
            print(f'The temperature in Celcius is : {temp}°C')
            os.system('pause')
            break
        else:
            print(f"{unit} is an invalid unit of measurement")


# Main Body
Menu = -1
while (Menu != 0):
    Menu = program_menu()

    if Menu == 1:
        print("\n-----------")
        weight()

    elif Menu == 2:
        print("\n-----------")
        temperature()

    else:
        print("[#19E62F]Thanks for using our program !![/]")
