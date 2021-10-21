def test():
    print("null")


# Exercise 1: Write a function named right_justify that takes a string,
# named `s` as a parameter and prints the string with enough,
# leading spaces so that the last letter of the string is in column 70,
# of the display.
def right_justify():
    s = "Test String leading space to be added."
    s_spaced = s.rjust(10)
    print(s_spaced)


## Add the space at Start of the string in Python
string2 = "Test String leading space to be added"
string_length = len(string2) + 10  # will be adding 10 extra spaces
print(type(string_length))
string_revised = string2.rjust(string_length)
print(string_revised)


if __name__ == '__main__':
    right_justify()
