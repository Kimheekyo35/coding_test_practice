n = int(input())

if n < 8:
    if n == 2:
        print(28)
    elif n%2!=0:
        print(31)
    else:
        print(30)
else:
    if n%2!=0:
        print(30)
    else:
        print(31)