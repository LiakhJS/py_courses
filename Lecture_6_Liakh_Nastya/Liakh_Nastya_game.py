import random as r


def game():
    rand_secret_number = r.randint(1,3)  # Случайное число от 1 по 3 включительно
    user_number = int(input("Дай число от 1 по 3 включительно:"))

    if rand_secret_number == user_number:
        print("ok")
    else:
        print("sorry")


game()