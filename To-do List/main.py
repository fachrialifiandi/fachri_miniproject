import os
from rich import print

list_items = []


os.system('cls')


def program_menu(Choice):

    while True:
        os.system('cls')
        print("To-Do List 📄")
        print('==============\n')
        print('1. Add list to do. ')
        print('2. See the list. ')
        print('3. Remove list to do. ')
        print('4. Out.')

        try:
            print('\n[#048ABF]Which one do you choose?[/] ', end="")
            Choice = int(input())
            if (Choice >= 1) and (Choice <= 4):
                return Choice

            else:
                print('\nYou choose wrong number, please press enter.')
                os.system('pause')
        except ValueError:
            print('\n[#C51F1A]Invalid input, please input a number.[/]')
            os.system('pause')


def add_list():

    print("[#048ABF]What list do you want to add?[/] ", end="")

    new_list = input()
    os.system('cls')

    list_items.append(new_list)
    print(f'[#048ABF]You receive new activity[/] {new_list}')

    os.system('pause')
    os.system('cls')


def all_list():
    # with out enumerate

    if not list_items:
        print('[#048ABF]There is no task in the list yet.[/]')

    else:
        i = 1
        for j in list_items:
            print(f"{i}. {j}")
            i += 1

    print("\n")
    os.system('pause')
    os.system('cls')

    # if not list_items:
    #     print('There is no task in the list yet')
    # else:
    #     for i, j in enumerate(list_items, start=1):
    #         print(f"{i}. {j}")

    # print("\n")
    # os.system('pause')
    # os.system('cls')


def remove_list():
    while True:
        os.system('cls')
        print('\n-- Remove List Menu --')
        print("===================\n")

        if not list_items:
            print('[#048ABF]There is no task in the list yet.[/]')
            os.system('pause')
            break

        else:
            print('Choose the number of task that you want remove: ')
            for i, j in enumerate(list_items, start=1):
                print(f"{i}. {j}")

            try:
                input_delete_items = int(input("\nInput task number: "))

                if input_delete_items >= 1 and input_delete_items <= (len(list_items)):

                    removed = list_items.pop(input_delete_items - 1)
                    print(f"\n[#C51F1A]Task {removed} just deleted.[/]")
                    os.system('pause')
                    break

                else:
                    print("[#C51F1A]Invalid number. Try again.[/]")
                    os.system('pause')
                    continue

            except ValueError:
                print('\n[#C51F1A]Invalid input, input a number.[/]')
                os.system('pause')
                continue

    print("\n")
    os.system('cls')


# Main Body
Menu = 0

while (Menu != 4):
    Menu = program_menu(Menu)
    os.system('cls')

    if (Menu == 1):
        print('-- Add List Menu --')
        print("===================\n")
        add_list()

    elif (Menu == 2):
        print('The List Remaining : ')
        print("===================\n")
        all_list()

    elif (Menu == 3):
        remove_list()

    else:
        print('Thanks for using this program !')
        print('Make sure you complete your work !!')
