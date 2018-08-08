"""
CP1404 Week 03 warmup
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number
The program should not allow an invalid age number
Re-prompt until a valid number is entered
"""


while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("Error.")

if age % 2 == 0:
    print("Even")
else:
    print("Odd")


def thingo():
    x = 4
    print(x)
    print(x)
    return x

# sales = 2345678
# sales = float(input("Enter sales: $"))
#
# if sales < 1000:
#     bonus = 0.1 * sales
# else:
#     bonus = 0.15 * sales
#
# print(bonus)
#
#
# if x:
#     pass
# else:
#     ...