from week_06.product import Product
INITIAL_NUMBER_OF_TACOS = 5


class User:
    def __init__(self, name="", score=0):
        self.name = name
        self.number_of_tacos = INITIAL_NUMBER_OF_TACOS
        self.score = score
        self._private = 0
        self.__hidden = 0

    def __str__(self):
        return "{self.name}, {self.score} points, {self.number_of_tacos} tacos left".format(self=self)

    def __repr__(self):
        return str(self)

    def give_taco(self, other, number_given=1):
        if number_given < 1:
            return
        if self.number_of_tacos < number_given:
            number_given = self.number_of_tacos
        self.number_of_tacos -= number_given
        other.score += number_given

    def steal_taco(self, other):
        self.score = 0


if __name__ == '__main__':
    user1 = User("Ben", 4)
    user2 = User("Margaret")
    user1.give_taco(user2, -200)
    print(user1)
    print(user2)
    user1.steal_taco(user2)
    assert user1.score == 0
