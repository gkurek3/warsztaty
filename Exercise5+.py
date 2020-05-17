import random

dice_list = ['D3', 'D4', 'D6', 'D8', 'D100', 'D10', 'D12', 'D20']


def cube(user_dice):
    """
    function imitates dice throw.

    :param user_dice:
    :return: result of dice throw
    """
    for dice in dice_list:
        if dice in user_dice:
            x = user_dice.split(dice)
            throw = random.randint(1, int(dice[1:]))
            try:
                if x[0]:
                    multiply = x[0]
                    multiply = int(multiply)
                else:
                    multiply = 1
            except ValueError:
                print("Niepoprawne dane")
                break
            try:
                if x[1]:
                    modifier = x[1]
                    modifier = int(modifier)
                else:
                    modifier = 0
            except ValueError:
                print("Niepoprawne dane")
                break
            my_list = []
            for i in range(multiply):
                my_list.append(throw)
            return sum(my_list) + modifier


print(cube('D3'))
print(cube('2D4+10'))
print(cube('2D6-20'))
print(cube('2D20+15'))
print(cube('2D100+100'))
print(cube('aD20+15'))
print(cube('2D100+b'))
