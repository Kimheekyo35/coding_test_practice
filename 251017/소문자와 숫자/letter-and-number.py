string = input()

for s in string:
    if s.isalpha():
        print(s.lower(),end="")
    elif s.isdigit():
        print(s,end="")