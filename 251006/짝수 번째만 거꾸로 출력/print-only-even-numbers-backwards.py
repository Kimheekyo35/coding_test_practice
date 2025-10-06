string = input()

for elem in range(len(string)-1,-1,-1):
    if (elem+1)%2 == 0 :
        print(string[elem],end='')