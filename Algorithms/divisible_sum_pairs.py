#!/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
for indexi, i in enumerate(a):
    for indexj, j in enumerate(a):
        if indexi < indexj and (i + j) % k == 0:
            count = count + 1

print(count)
