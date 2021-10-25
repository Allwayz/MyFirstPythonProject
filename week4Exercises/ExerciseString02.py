def fileReader():
    fin = open('exerciseFiles/words.txt')
    for eachLine in fin.readlines():
        if len(eachLine) > 20:
            print(eachLine)


def has_no_e():
    def calculate_percentage(total_count, counter):
        return counter / total_count

    fin = open('exerciseFiles/words.txt')
    count = 0
    total = 0
    for eachLine in fin.readlines():
        total = total + 1
        if "e" not in eachLine:
            print(eachLine)
            count = count + 1
    return calculate_percentage(total, count)


if __name__ == '__main__':
    # fileReader()
    print("Percentage is", float(has_no_e()) * 100, "%")
