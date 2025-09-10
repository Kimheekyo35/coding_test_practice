import sys
n=int(input())

arr=list(map(int,input().split()))

cnt_list=[]
for i,val in enumerate(arr) :
    if val==2:
        cnt_list.append(i)

for idx,ele in enumerate(cnt_list):
    if idx==2:
        print(ele+1)