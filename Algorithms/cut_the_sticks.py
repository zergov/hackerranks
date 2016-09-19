#!/bin/python3


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

done = False
while not done:

    # Get the smallest stick in the pack of sticks
    smallest = None
    done = True
    size = 0
    for stick in arr:
        if stick > 0:
            done = False
            size = size + 1
            if smallest is None or stick < smallest:
                smallest = stick

    if done: # if we're done, break here.
        break

    print(size)

    # cut the sticks.
    for i, stick in enumerate(arr):
        arr[i] = stick - smallest
