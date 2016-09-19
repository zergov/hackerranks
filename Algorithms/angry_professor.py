#!/bin/python3


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]

    present = 0
    for i, student in enumerate(a):

        # initial check to see if the threshold is meet
        if present >= k:
            print('NO')
            break;

        # initial check to see if there's enough student
        # left in the class to satisfy the threshold requirements
        if present + (n - (i + 1)) < k:
            print('YES') # class is canceled
            break

        if student <= 0:
            present = present + 1
