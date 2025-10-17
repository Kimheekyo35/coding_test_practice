string1 = input()
string2 = input()

count = 0
while True:
    
    if string1 == string2:
        break
    else:
        string1 = string1[-1] + string1[:-1] 
        count += 1
    if count > len(string1):
        count = -1
        break

print(count)