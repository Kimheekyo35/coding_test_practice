n = int(input())

# 0 1 2 3
# 0
#   1
#     2
#       3
# 우선 2행 2열까지, 4행 4열까지, 6행 6열까지 정사각형으로 출력하는 것 같음
# 근데 1행을 어떻게 채우는 지 모르겟음.. -> j = 0, i = 0 이랑 i<=j 로 *채움
# i, j의 행렬 기준이 뭔지 모르겠음. -> j가 열, i는 행

# i = 0,1
# for i in range(n):
#     for j in range(n):
#         # j는 열
#         if j%2 == 0:
#             if i == 0:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if i<=j:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")

#     print()



# 0 1,2,3
# 1
# 2
# 3
for i in range(n):
    for j in range(n):
        # 열이 짝수일 때
        if j % 2 == 0:
            if i == 0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        # 열이 홀수 일 때
        else:
            if i<=j :
                print("*",end=" ")
            else:
                print(" ",end=" ")

        
        

        
    print()





























