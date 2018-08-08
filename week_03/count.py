
def count_letters(text):
    count = 0
    for character in text:
        count = 0
        if character.isalpha():
            count += 1
    return count


# print(count_letters(""))
# print(count_letters("abc"))
# print(count_letters("123"))

strings = ["blah", "and 1", "..."]
for string in strings:
    print(count_letters(string))

assert count_letters("a") == 1
assert count_letters("ab") == 2
