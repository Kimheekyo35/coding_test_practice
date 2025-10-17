string_list = []
count = 0

for _ in range(200):
    string = input()
    if string.isalpha():
        count += 1
    else:
        break
    if (count % 2) != 0:
        string_list.append(string)
    
print(count)
for s in string_list: print(s)