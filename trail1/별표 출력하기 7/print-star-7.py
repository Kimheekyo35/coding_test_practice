n = int(input())

for i in range(1,n+1):
    # 여기서 j는 필요없으므로 j는  _로 둬도 됨
    for j in range(1,i+1):
        print("*",end=" ")
    print()
