string1 = input()
string2 = input()

num1 = ""
num2 = ""

for s in string1:
    if s.isdigit():
        num1 += s
    else:
        pass

for s in string2:
    if s.isdigit():
        num2 += s
    else:
        pass

print(int(num1) + int(num2))