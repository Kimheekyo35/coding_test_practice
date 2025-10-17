string = input()

for s in string:
    if s.isalpha():
        if ord(s) >= 65 and ord(s) <= 96:
            print(s.lower() , end = "")
        elif ord(s) >= 97:
            print(s.upper() , end = "")