#!/bin/python3


def digitsum(n, k):
    if n < 10 and k == 1:
        return n
    else:
        total = 0
        while n > 0:
            total = total + (n % 10)
            n = n // 10
        return digitsum(total * k, 1)


if __name__ == '__main__':
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]

    print(digitsum(n, k))
