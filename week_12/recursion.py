def factorial(n):
    """Calculate the factorial of n recursively."""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


def print_down(n):
    for i in range(n, -1, -1):
        print(i)

# print_down(4)
