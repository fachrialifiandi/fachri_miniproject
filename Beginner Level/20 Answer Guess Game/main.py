from google import genai

client = genai.Client(api_key="AIzaSyCg2tD5S-sCQPaalOLgt4HMVM1Aq8ytlaE")


def main():

    print('Try and guess my animal!')

    animal = ask_genai('Return a random animal')

    for i in range(20):
        # clasically 20 questions long
        n_left = 20 - i
        question = input(
            f"You have {n_left} question left. Enter a question: ")
        prompt = build_promt(animal, question)
        answer = ask_genai(prompt)
        print(answer)

        if answer == "You guessed it 🧠":
            print("Congratulation You Win !")
            break


def ask_genai(prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )

    return response.text


def build_promt(animal, question):
    return f""" You are a helpful assistant playing a game of 20 questions. You will be given a question and you need to answer in a way
    helpful for the user.
    
    The user is trying to guess your secret animal: {animal}.
    
    They just asked the question:{question}
    
    Important !! Do not mention the {animal} in your response, unless the user has guessed it.
    If the user has guessed the animal, respond with "You guessed it 🧠" and the game is over.

    """


if __name__ == "__main__":
    main()
