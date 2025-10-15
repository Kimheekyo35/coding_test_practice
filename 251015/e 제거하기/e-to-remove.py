string = input()

for i in string:
    if i == 'e':
        idx = string.index(i)
        break

print(string[:idx]+string[idx+1:])