question = ['what is your name', 'how old are you', 'what is your favorite food',
            'where do you come from', 'what is the name of your capital city',
            'what is your religion']
answers = ['Tony', '23years', 'gari', 'Sunyani', 'Accra', 'christian']


def nation():
    print("Welcome to COCOBOD INTERVIEW.")
    correct_guess = 0

    for question_num, actual_question in enumerate(question):
        print(f"{question_num + 1}:{actual_question}")
        ans = input("enter your answer:").lower()
        if ans == answers[question_num].lower():
            print("correct")
            correct_guess += 1
        else:
            print("incorrect")
    print(f"score is:{correct_guess}/{len(question)}")
    if correct_guess >= 3:
        print("Passed Interview")
    else:
        print("Failed Interview")


nation()
