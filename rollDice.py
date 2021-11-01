import random


def test(input_inter):
    for i in range(0, input_inter):
        print(i)


def draw_dice(spots):
    print("+-------+")
    if spots == 1:
        print("     ")
        print("  *  ")
        print("     ")
    elif spots == 2:
        print("  *  ")
        print("     ")
        print("  *  ")
    elif spots == 3:
        print("  *  ")
        print("  *  ")
        print("  *  ")
    elif spots == 4:
        print(" * * ")
        print("     ")
        print(" * * ")
    elif spots == 5:
        print(" * * ")
        print("  *  ")
        print(" * * ")
    elif spots == 6:
        print("* * *")
        print("* * *")
        print("* * *")
    else:
        print("Error: illegal dice value")
    print("+-------+")


def roll():
    return random.randrange(1, 7)


def main():
    print("How many dice do you want to roll?")
    number_of_rolls = input()
    number_of_rolls_as_int = str(number_of_rolls)
    for i in range(1, number_of_rolls_as_int):
        number_of_spots = roll()
        draw_dice(number_of_spots)


if __name__ == '__main__':
    # main()
    test(4)
