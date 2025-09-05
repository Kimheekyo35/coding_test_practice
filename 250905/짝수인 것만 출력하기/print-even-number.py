n=int(input())
arr=list(map(int,input().split()))

new_list=[print(arr[i],end=' ') for i in range(len(arr)) if (i+1)%2==0]