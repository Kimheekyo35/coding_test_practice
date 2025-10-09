arr = input()
per = input()

idx = -1
for i in range(len(arr)-len(per)+1):
    if per in arr:
        idx = arr.index(per)
        break

print(idx)
