string1 = input()
string2 = input()

for str1 in string1:
    if ' ' in str1:
        continue
    print(str1,end='')

for str2 in string2:
    if ' ' in str2:
        continue
    print(str2, end='')