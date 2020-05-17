def guess():
    """
    Function guesses the number the user thinks about.
    User types str to guide program if his guesses are too small or too big.

    :rtype: str
    :return: str if users number is guessed
    """
    print("Think of a number between 0 and 1000.")
    print("Press 'ENTER' to continue")
    input()
    min = 0
    max = 1000
    while True:
        guess = int((max - min) / 2) + min
        possible_answers = ['too big', 'too small', 'you win']
        answer = input(f"My guess: {guess}. Am I right?")
        if answer in possible_answers:
            if answer == "too big":
                max = guess
            elif answer == "too small":
                min = guess
            elif answer == "you win":
                return "I've won! Thanks for the game."
        else:
            print("Possible answers are: 'too big', 'too small', 'you win'. Try again.")
            continue


print(guess())
