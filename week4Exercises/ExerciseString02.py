def fileReader():
    fin = open('exerciseFiles/words.txt')
    for eachLine in fin.readlines():
        if len(eachLine) > 20:
          print(eachLine)

def has_no_e():
    fin = open('exerciseFiles/words.txt')


if __name__ == '__main__':
    fileReader()