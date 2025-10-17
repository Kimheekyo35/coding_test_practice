string = input()

for s in string:
    if ord(s) >= 72:
        print(s.upper(),end="")