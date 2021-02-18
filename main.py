import random as rnd

secret = rnd.randint(0, 100)

check = False

for i in range(7):
    guess_number = int(input("Enter your guess number: "))
    if guess_number == secret:
        print("Congrats!!!")
        check = True
        break
    elif guess_number < secret:
        print("Enter a greater number: ")
    else:
        print("Enter a smaller number: ")

if not check:
    print("You did not find this number -->", secret)
