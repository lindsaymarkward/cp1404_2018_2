things = "10, 2, 3, 4, -15, 6".split(", ")
# print(things)

# print(sum((1 for thing in things if len(thing) > 1)))


def fn(a, b, *c):
    print(a, b, c)


fn(1, 2)


# print(sum(counts))
# numbers = []
# for thing in things:
#     if int(thing) > 3:
#         numbers.append(int(thing))

# numbers = [int(thing) for thing in things if int(thing) > 3]

# print(numbers)

# words = 'one two three'.split()
# for word in words:
#     word = word.title()
#     print(id(word))
# print()
#
# for i in range(len(words)):
#     # words[i] = words[i].title()
#     print(id(words[i]))
#
# print(words)
