string = input()
point = string[1]
change = string[0]
for i in range(len(string)):
    
    if string[i] == point:
        string = string[:i] + change + string[i+1:]
    
print(string)