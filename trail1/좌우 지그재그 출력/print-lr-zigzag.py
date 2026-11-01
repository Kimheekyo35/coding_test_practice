n = int(input())
cnt = 1

for i in range(n):
    reverse_list = []
    if i%2 == 0:
        for j in range(n):
            print(cnt,end=" ")
            cnt += 1
    else:
        for j in range(n-1,-1,-1):
            reverse_list.append(cnt)
            cnt += 1
        [print(r,end=" ") for r in reverse_list[::-1]]
            
    print()

    
    