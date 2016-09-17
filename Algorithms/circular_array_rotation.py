#!/bin/python3

# n = length of array
# k = how many times we repeat the circular rotation
# q = number of queries
n, k, q = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# initial array
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# index to look for
queries = []
for i in range(q):
    queries.append(int(input().strip()))

# circular rotation
for _ in range(k % n):
    arr.insert(0, arr.pop())

# printing
for q in queries:
    print(arr[q])
