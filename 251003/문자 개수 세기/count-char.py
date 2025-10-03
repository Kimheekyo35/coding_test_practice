string = input()
point = input()

num = 0

for string_i in string:
    if point == string_i:
        num+=1

print(num)