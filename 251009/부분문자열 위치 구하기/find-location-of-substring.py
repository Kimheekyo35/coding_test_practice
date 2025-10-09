import sys

arr = input()
per = input()

idx = -1

if per in arr:
    idx = arr.index(per[0])

print(idx)
