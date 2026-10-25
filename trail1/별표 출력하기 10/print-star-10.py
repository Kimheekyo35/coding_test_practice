# n = int(input())
# first = 1
# second = n
# for i in range(1,2*n+1):
#     # 1,3,5
#     if i%2:
#         for _ in range(first):
#             print("*",end=" ")
#         print()
#         first += 1
#     # 2,4,6
#     else:
#         # second는 -1 이 계속 되므로 (second,0,-1)을 적지않아도 됨.
#         for _ in range(second):
#             print("*",end=" ")
#         print()
#         second -= 1

n = int(input())
# 0,1,2,3,4,5
for i in range(2*n):
    # 0,2,4
    if i%2==0:
        for i in range(1+i//2):
            print("*",end=" ")
        print()

    else:
        # 3-0, 3-1, 3-2
        for i in range(n-(i//2)):
            print("*",end=" ")
        print()