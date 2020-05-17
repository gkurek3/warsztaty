import random


def typing_numbers():
    """
    Get numbers from user.
    Check if number is int, is unique and between 1 and 49.

    :rtype: int
    :return: list of given numbers
    """
    user_numbers = []
    i = 0
    while i < 6:
        try:
            given_number = int(input("Wytypuj 6 liczb od 1 do 49: "))
        except ValueError:
            print("Miała być liczba!")
            continue
        if given_number in user_numbers:
            print("Podałeś tą liczbę wcześniej. Podaj inną.")
        elif given_number not in range(1, 49):
            print("Podałeś liczbę spoza zakresu 1-49. Spróbuj jeszcze raz.")
        else:
            user_numbers.append(given_number)
            i += 1
    return user_numbers


def lotto():
    """
    Draws random numbers between 1 and 49.
    Sorts user's and drawn numbers.
    Checks for elements in both lists that are the same.

    :return: number of matched numbers
    """
    user_numbers = typing_numbers()
    draw_numbers = random.sample(range(1, 49), 6)
    user_numbers.sort()
    draw_numbers.sort()
    print(f"Wytypowane liczby to: {user_numbers}")
    print(f"Wylosowane liczby to: {draw_numbers}")
    user_numbers = set(user_numbers)
    draw_numbers = set(draw_numbers)
    matched_numbers = len(user_numbers & draw_numbers)
    if matched_numbers > 0:
        return f"Trafiłeś {matched_numbers} liczby."
    else:
        return f"Nie trafiłeś ani jednej liczby."


print(lotto())
