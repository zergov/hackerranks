#!/bin/python3

n = int(input().strip())

for v in range(n):
    spaces = ' ' * (n - (v+1))
    symbol = '#' * (v + 1)
    print(spaces + symbol)
