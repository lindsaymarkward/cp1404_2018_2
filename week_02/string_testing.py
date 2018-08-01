
# determine if a given string contains any capitals
string = input("Enter: ")
# string = "like this Y'all OK"
# string = "like"

has_capital = False
for character in string:
    if character.isupper():
        has_capital = True
        break
if has_capital:
    print("Yes")
else:
    print("No")

# string formatting
for i in range(0, 13, 3):
    print("{:02}".format(i))


name = "Monty"
money = 75.3

print("{0} has ${1:.2f}".format(name, money))
