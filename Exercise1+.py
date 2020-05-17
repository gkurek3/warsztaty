import random


def guess_number():
    """
    Function draws random number,
    takes number from a user and checks if they match.

    :return: str "You win!" if numbers are the same
    """
    searched_number = random.randint(1, 10)
    while True:
        try:
            users_number = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")
            continue
        if users_number > searched_number:
            print("Too big!")
        elif users_number < searched_number:
            print("Too small!")
        else:
            return "You win!"


print(guess_number())
