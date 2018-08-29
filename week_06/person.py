class Person(object):
    def __init__(self, name="", gender=""):
        self.name = name


class Student(Person):
    def __init__(self, name="", gender="", student_id=""):
        Person.__init__(self, name, gender)
        self.id = student_id

    def __str__(self):
        return Person.__str__(self) + "\nID: " + self.id

    def get_id(self):
        return self.id


x = 3
if isinstance(x, float):
    print("float")
else:
    print(type(x))
