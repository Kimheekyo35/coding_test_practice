string = input()

for s in string:
    if ord(s) >= 65:
        print(s.upper(),end="")