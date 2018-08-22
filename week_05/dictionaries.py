"""CP1404 2018-2 Week 05 Dictionaries demos."""


def main():
    # names = ["Bill", "Jane", "Sven"]
    # ages = [21, 34, 56]
    names = []
    ages = []
    print(find_oldest(names, ages))


def find_oldest(names, ages):
    highest_age = -1
    highest_age_index = -1
    for i, age in enumerate(ages):
        if age > highest_age:
            highest_age = age
            highest_age_index = i
    return names[highest_age_index]


main()
