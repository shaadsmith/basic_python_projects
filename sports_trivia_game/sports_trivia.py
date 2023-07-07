print('WELCOME TO SPORTS TRIVIA! \n')

play = input("Would you like to play? (Y/N) ")

if play.lower() != "y":
    print("OK, maybe some other time!")
    quit()
else:
    print("Great! Time to test your knowledge! \n")

question_num = 1

print(f'Question #{question_num}')
answer = input("Who is the All-Time leading scorer in the NBA? \n A. Michael Jordan \n B. Lebron James \n C. Kareem Abdul-Jabbar \n D. Steph Curry \n Answer: ")
if answer.upper() == 'B':
    print(f'Nice, {answer.upper()} is the correct answer \n')
else:
    print(f'Sorry, {answer.upper()} is the wrong answer \n')

question_num += 1

print(f'Question #{question_num}')
answer = input("What MLB team has the most World Series titles? \n A. Yankees \n B. Giants \n C. Dodgers \n D. Braves \n Answer: ")
if answer.upper() == 'A':
    print(f'Nice, {answer.upper()} is the correct answer \n')
else:
    print(f'Sorry, {answer.upper()} is the wrong answer \n')