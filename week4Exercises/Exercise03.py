def print_mash(element1, element2):
    dash = '|'
    dash_length = len(dash) + 5
    mid_dash = dash.rjust(dash_length)

    for i in range(11):
        if 1 == i + 1 or 5 == i + 1 or 11 == i + 1:
            print(element1, element2 * 4, element1, element2 * 4, element1)
        else:
            print(dash, mid_dash, mid_dash)


if __name__ == '__main__':
    print_mash('+', '-')
