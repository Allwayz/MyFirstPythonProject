# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')


# exercise 17: Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user.
def check_odd_or_even(input_number):
    # input_number = float(input("input a number"))
    if input_number % 2 == 0:
        print(f"number {input_number} is even")
    else:
        print(f"number {input_number} is odd")

# exercise 18: Write a Python program to calculate the body mass index (BMI).
def bmi_calculator(mass,height):
    BMI = mass/height**2
    print(BMI)

# exercise 19: Write a Python program to convert any number of days, hours, minutes and seconds into second.
def second_convertor(day,hours,minutes,seconds):
    result = day*24*60*60 + hours*60*60 + minutes*60 + seconds
    result_e = ((day*24+hours)*60+minutes)*60+seconds
    print(result,result_e)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #check_odd_or_even(float(input("input a number: ")))
    #bmi_calculator(float(input("input mass: ")),float(input("input height: ")))
    second_convertor(int(input("input day: ")),int(input("input hours: ")),int(input("input minutes: ")),int(input("input seconds: ")))
    # print_hi('PyCharm')

