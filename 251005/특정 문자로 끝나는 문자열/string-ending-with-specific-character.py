arr = [input() for _ in range(10)]
n = input()
state = False
for string in arr:
    if string[-1] == n:
        state = True
        print(string)

if state:
    pass
else:
    print("None")
