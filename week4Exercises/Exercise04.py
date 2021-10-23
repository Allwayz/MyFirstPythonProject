import math
import os
from prettytable import PrettyTable


def mysqrt(userInput):
    mySqrtList = list()
    x = 1
    for a in range(1, userInput):
        while True:
            print(x)
            y = (x + a / x) / 2
            if abs(y - x) < 0.0000001:
                break
            x = y
        mySqrtList.append(y)
    print('--------------------------')
    # print(mySqrtList)
    return mySqrtList


def test_square_root(userInput):
    squareList = list()
    for a in range(1, userInput):
        squareList.append(math.sqrt(a))
    return squareList


if __name__ == '__main__':
    squareRange = int(input("Enter A number: "))+1
    mysqrtList = mysqrt(squareRange)
    test_square_root_list = test_square_root(squareRange)

    # os.system("clear")
    table = PrettyTable(['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'])
    for a in range(1,squareRange):
        table.add_row([a,mysqrtList[a-1],test_square_root_list[a-1],abs(mysqrtList[a-1] - test_square_root_list[a-1])])

    print(table)