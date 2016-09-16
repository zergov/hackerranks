#!/bin/python3

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum = 0
for i, row in enumerate(a):
    sum = sum + row[i]

for i, row in enumerate(a):
    sum = sum - row[(n - 1) - i]

print(abs(sum))
