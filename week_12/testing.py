import doctest


def create_empty_list():
    return []


x = create_empty_list()
assert x == [], "empty borked"


def is_odd(n):
    return n % 2 == 1


assert is_odd(3)
assert not is_odd(4)


def is_adult(age):
    """
    Determine if age represents an adult (QLD Age of Majority Act 1974)
    >>> is_adult(7)
    False
    >>> is_adult(40)
    True
    >>> is_adult(18)
    True
    """
    return age >= 18


def get_middle(values):
    """
    >>> get_middle([1, 2])
    1
    >>> get_middle("abc")
    'b'
    """
    pass


doctest.testmod()
