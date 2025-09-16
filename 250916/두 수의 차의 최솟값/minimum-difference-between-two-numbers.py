
n=int(input())

arr=list(map(int,input().split()))

min_val=99
# for i in range(n):
#     for j in range(i+1,n):
#         if min_val>arr[j]-arr[i]:
#             min_val=arr[j]-arr[i]

# print(min_val)

for i in range(n-1):
    if min_val>arr[i+1]-arr[i]:
        min_val=arr[i+1]-arr[i]
print(min_val)


# 오름차순이라는 말 중요!!
# 오름차순이므로 인접한 두 값의 차가 가장 작음.