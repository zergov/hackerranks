#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


positive = negative = zeros = 0
for i in arr:
    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1
    else:
        zeros = zeros + 1

# test cases are scaled to 6th decimal
PRECISION = '.6f'
print(format(float(positive / n), PRECISION))
print(format(float(negative / n), PRECISION))
print(format(float(zeros / n), PRECISION))
