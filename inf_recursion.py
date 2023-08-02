import sys


def get_recursive_depth():
    print(sys.getrecursionlimit())


def set_recursive_depth(value: int):
    sys.setrecursionlimit(value)


def inf_counter(i: int):
    print(i)
    return inf_counter(i + 1)


if __name__ == '__main__':
    # inf_counter(1)

    set_recursive_depth(2000)
    inf_counter(1)

    set_recursive_depth(1000)
