n=int(input())
arr=list(map(int,input().split()))

new_list=[print(i,end=' ') for i in arr if i%2==0 ]