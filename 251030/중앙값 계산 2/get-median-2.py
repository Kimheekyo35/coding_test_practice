n = int(input())
arr = [0]+list(map(int,input().split()))
# Please write your code here.

for i in range(1,n+1):
    if i % 2 != 0:
        arr2 = arr[1:i+1]
        arr2.sort()
        print(arr2[i//2],end=" ")
        

