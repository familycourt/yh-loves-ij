import sys


def print_star(count):
    for i in range(1, count + 1):
        print(" " * (count - i), end="")
        print("*" * (i * 2 - 1))


N = int(sys.stdin.readline())

print_star(N)
