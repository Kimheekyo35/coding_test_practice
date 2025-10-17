A = input()

number = 0
for a in A:
    if a.isdigit():
        number += int(a)

print(number)