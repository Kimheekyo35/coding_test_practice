N = int(input())

for i in range(1,N+1):
    if i%2==0 or i==5 or i%10==5 or i%100==5 or (i%3==0 and i%9):
        continue
    print(i,end=" ")

