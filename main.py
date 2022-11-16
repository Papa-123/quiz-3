import time
time.sleep(1)
print("Welcome to a very interesting quiz")
chances = 1
print("You will have", chances, "chance to answer correctly.\nPlease speak to answer\n")
time.sleep(2)
score = 0
question_1 = print(" 1) What type of weapon does Nobara use to exorcise curses in Jujutsu Kaisen?\n(a) Hammer \n(b) Sword \n(c) Belt \n(d) Salt \n\n")
answer_1 = "a"

for i in range(chances):
    answer = input("Enter ur choice:")
    if (answer.lower()  == answer_1):
        print("Correct!\n")
        score = score +1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

question_2 = print(" 2) Who is the cyborg character in One Puch Man?\n(a) Saitama \n(b) Fang \n(c) Mumen Rider \n(d) Genos \n\n")
answer_2 = "d"

for i in range(chances):
    answer = input("Enter ur choice:")
    if (answer.lower()  == answer_2):
        print("Correct!\n")
        score = score +1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

question_3 = print(" 3) Who is Gojo fighting when he teaches Itadori about domain expansion?\n(a) Jogo \n(b) Mahito \n(c) Sugugru Geto \n(d) Vortex \n\n")
answer_3 = "a"

for i in range(chances):
    answer = input("Enter ur choice:")
    if (answer.lower()  == answer_3):
        print("Correct!\n")
        score = score +1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

question_4 = print(" 4)Where did Itadori and Nanami investigate the massacre by Mahito?\n(a) Movie Theater \n(b) Mall \n(c) Grocery Store \n(d) Pub \n\n")
answer_4 = "a"

for i in range(chances):
    answer = input("Enter ur choice:")
    if (answer.lower()  == answer_4):
        print("Correct!\n")
        score = score +1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

while score>=2:
    print("Well Done! Your score was",score)
    break
while score<2:
    print("Better Luck next time! Your score was", score)
    break
