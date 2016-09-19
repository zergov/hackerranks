#!/bin/python3

x1, v1, x2, v2 = [int(arr_temp) for arr_temp in input().strip().split(' ')]

try:
    if abs((float(x2 - x1) % float(v1 - v2))) == 0:
        steps = abs((float(x2 - x1) / float(v1 - v2)))
        at_same_time = v1 * steps + x1 == v2 * steps + x2
        print('YES' if at_same_time else 'NO')
    else:
        print('NO')
except Exception:  # lol
        print('NO')
