def countString():
    stringInput = "banana"
    print(stringInput.count('a'))


def stringSlice():
    string_input = "apple"
    print(stringInput[0:len(stringInput):2])


def rotate_word(input_string, integer):
    encrypted_string = str()
    for char in input_string:
        print(chr(ord(char) - integer))
    # print(ord('z'),ord('Z'),ord('A'))
    # print(chr(97))
    return "sss"


if __name__ == '__main__':
    # countString()
    # stringSlice()
    rotate_word("apple", 1)
