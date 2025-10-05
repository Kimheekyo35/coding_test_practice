string = input()

num = int(input())

for i in range(len(string)-1,-1,-1):
    if num > len(string):
        print(string[i], end='')
    else:
        print(string[i],end='')
        if i == len(string)-num :
            break