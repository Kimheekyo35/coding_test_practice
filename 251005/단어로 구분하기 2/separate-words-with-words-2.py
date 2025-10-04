string = input().split()

for elem in string:
    if string.index(elem)%2 == 0:
        print(elem)