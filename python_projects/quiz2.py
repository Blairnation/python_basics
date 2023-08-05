questions = {
    "Who is the president of Ghana": "A",
    "What is my name": "C",
    "What is the name of this institution": "A"
}
options = [["A. H.E Nana Addo", "B. H.E John Mahama", "C. H.E Kuffour"],
           ["A. Blair", "B. Nation", "C. Tony"],
           ["A. UENR", "B.UCC", "C.UMAT"]]


def new_game():
    print("Welcome to Blair's Interview")
    print('-------------------')
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A,B,C)").upper()
        guesses.append(guess)
        question_num += 1

        correct_guesses += check_answer(questions.get(key), guess)
        display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_score, guesses):
    print("-------------")
    print("Quiz results")
    print("Your guess", guesses)
    print("The Correct answers were", [questions[c] for c in questions])
    print("score: ", correct_score, "/", len(questions))
    print("-------------")
    if correct_score == 3:
        print("Good Job")
    elif correct_score >= 2:
        print("Room for improvement")
    else:
        print("Fail")


new_game()
