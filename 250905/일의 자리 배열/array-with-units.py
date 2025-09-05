# arr=list(map(int,input().split()))


# p=arr[1]
# pp=arr[0]
# for _ in range(3,11):
#     pp,p=p,pp+p
#     if p and pp not in arr:
#         arr.append(pp)
#         arr.append(p)

# for i in arr:
#     print(i%10,end=' ')

p1,p2=map(int,input().split())

#우선 공백으로 리스트 만들어줌
arr=[0]*10
arr[0]=p1
arr[1]=p2

for i in range(2,10):
    arr[i]=(arr[i-1]+arr[i-2])%10

for ele in arr:
    print(ele,end=' ')