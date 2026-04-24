choices = ('r', 'p', 's')
user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
if user_choice not in choices:
    print("Invalid choice!")