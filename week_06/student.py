"""Student class."""


class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id
        self._special = True
        self.__secret = ":)"

    # def __str__(self):
    #     return "{} {} ({})".format(self.first_name, self.last_name, self.id)

    def get_full_name(self):
        return self.first_name + " " + self.last_name


if __name__ == '__main__':
    s1 = Student("Lindsay", "Ward", 123)
    print(s1.first_name)

    # print(s1._special)
    # print(s1.__secret)
    # print(s1._Student__secret)
    # print(s1.__dict__)
    # s1.graduate()
    # s2 = Student("Bob", "Marley")
    # s2.party()
    # print(s1.get_full_name())
    # print(s2.get_full_name())

