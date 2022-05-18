import random
import sys


def print_args(*args: str) -> None:
    strings = [a for a in args if a.isalpha()]
    numbers = [a for a in args if a.isnumeric()]
    numbers.sort()
    for _ in range(10):
        random.shuffle(strings)
        print(*strings, *numbers)


if __name__ == "__main__":
    if not sys.argv[1:]:
        print("There are no arguments provided")
    else:
        print_args(*sys.argv[1:])
