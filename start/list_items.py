questions = {
    "Who is the president of Ghana": "A",
    "What is my name": "B",
    "What is the name of this institution": "A"
}
options = [["A. H.E Nana Addo", "B. H.E John Mahama", "C. H.E Kuffour"],
           ["A. Blair", "B. Tony", "C. Yeboah"],
           ["A. UENR", "B.UCC", "C.UMAT"]]
choice = []
index = 0
correct_guess = 0
for question, answer in questions.items():
    print(question)
    for option in options[index]:
        print(option)
    index += 1
    guess = input("Choose option A,B or C: ").upper()
    choice.append(guess)
    if guess == answer:
        print("Correct")
        correct_guess += 1
    else:
        print("Wrong")
print(correct_guess)
print(choice)
print("correct answers are", [questions.get(answers) for answers in questions])
