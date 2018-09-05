from operator import attrgetter
from random import randint
from week_06.user import User


def main():
    names = "Ben", "Margaret", "Jane", "Nuno"
    users = []
    for name in names:
        score = randint(0, 50)
        users.append(User(name, score))
    print(users)
    users.sort(key=attrgetter("score", "name"), reverse=True)
    print(users)


main()
