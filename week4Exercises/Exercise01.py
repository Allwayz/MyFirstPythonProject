def test():
    print("null")


# Exercise 1: Write a function named right_justify that takes a string,
# named `s` as a parameter and prints the string with enough,
# leading spaces so that the last letter of the string is in column 70,
# of the display.
def right_justify():
    s = "Test String leading space to be added."
    s_length = len(s) + (70 - len(s))
    s_spaced = s.rjust(s_length)
    print(s_spaced)



if __name__ == '__main__':
    right_justify()
