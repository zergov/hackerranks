#!/bin/python3

from datetime import datetime

time = input().strip()
time = datetime.strptime(time, '%I:%M:%S%p')
print(time.strftime('%H:%M:%S'))
