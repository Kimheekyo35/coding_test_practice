string = input()
len_string = len(string)

for i in range(len_string+1):
    
    if i%5 == 0:
        print(string)
    else:
        string = string[-i] + string[i:]
    print(string)