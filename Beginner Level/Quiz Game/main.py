import os
os.system('cls')

questions = ("How many elements are in the period table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abudant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A.115", "B.127", "C.118", "D.119"),
           ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
           ("A.Nitrogen", "B.Oxygen", "C.Carbon-Dioxide", "D.Hydrogen"),
           ("A.206", "B.180", "C.211", "D.174"),
           ("A.Venus", "B.Mercury", "C.Earth", "D.Moon"))

answers = ("C", "D", "A", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print('----------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT !!')
    else:
        print("INCORRECT !!")
        print(f"The answer is {answers[question_num]}")
    question_num += 1

print('----------------------------------------')
print('                 RESULT                 ')
print('----------------------------------------')

print('answers: ', end="")
for answer in answers:
    print(answer, end="")
print()

print('guesses: ', end="")
for guess in guesses:
    print(guess, end="")
print()

score = score / len(questions) * 100
print(f'Your score is: {score}%')
