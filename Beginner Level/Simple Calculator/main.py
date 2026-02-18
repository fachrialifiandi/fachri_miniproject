import os
from rich import print

while True:

    os.system('cls')
    operator = print('[#048ABF]Enter an operator[/] (+ - * /): ', end="")
    operator = input()

    num1 = print('[#048ABF]Enter the 1st number:[/] ', end="")
    num1 = float(input())

    num2 = print('[#048ABF]Enter the 2nd number:[/] ', end="")
    num2 = float(input())

    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print('[#C51F1A]Please input the right operator! [/]')
        os.system('pause')
        continue

    else:

        if operator == "+":
            result = num1 + num2
            print(round(result, 3))

        elif operator == "-":
            result = num1 - num2
            print(round(result, 3))

        elif operator == "*":
            result = num1 * num2
            print(round(result, 3))

        elif operator == "/":
            result = num1 / num2
            print(round(result, 3))

    break
