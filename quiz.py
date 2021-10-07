print("Welcome To My Quiz Game !")
score = 0
player = input("Do you play this game !? Yes/No :")

if player.casefold() != "yes":
    exit()
else:
    print(">>>>> Game start !")

answer = input("Type One High Level Programming Language Name :")

high_Laval = ("Python", "Java", "C++", "C#","Visual Basic", "JavaScript", "php", "rust")

if answer.casefold() in high_Laval:
    print(f"This answer {answer} is >> Correct :)")
    score += 1
else:
    print("Incorrect Answer :(")

questions = {
    'Who is the father of C language?': "Dennis Ritchie",
    'Which of the following is not a valid C variable name? ': "int $main;",
    ' All keywords in C are in ____________ ': "LowerCase letters",
    'Which of the following is true for variable names in C? ': "Variable names cannot start with a digit",
    'Which is valid C expression? ': "int my_num = 100000;"
}

for k, v in questions.items():
    answer = input(f"{k} : ")
    vLow = str(v.casefold())
    if answer.casefold() == vLow:
        print(f"This answer {answer} is >> Correct :)")
        score += 1
    else:
        print(f"Incorrect Answer :( & The correct answer is >>> {vLow}")

if score <= 0:
    print("Your Correct Score Is 0")
else:
    print(f"Your Correct Score Is {score}")
