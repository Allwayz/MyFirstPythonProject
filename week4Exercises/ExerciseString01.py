def countString():
    stringInput = "banana"
    print(stringInput.count('a'))

def stringSlice():
    stringInput = "apple"
    print(stringInput[0:len(stringInput):2])


def rotate_word(inputString,Integer):
    encryptedString = str()
    for char in inputString:

        print(chr(ord(char) - Integer))
    # print(ord('z'),ord('Z'),ord('A'))
    # print(chr(97))
    return "sss"

if __name__ == '__main__':
    #countString()
    #stringSlice()
    rotate_word("apple", 1)