A = input()
B = input()

# len_a = len(A)
# len_b = len(B)

# while True:
#     idx = -1

#     candidates = len_a - len_b + 1

#     for i in range(candidates):
#         is_same = True
#         for j in range(len_b):
#             if A[i+j] != B[j]:
#                 is_same = False
#                 break
#         if is_same:
#             idx = i
#             # 이 for문에서 탈출
#             break
    
#     if idx == -1:
#         break

#     # B의 길이가 유동적일 수도 있으니까 idx+2 로 고정하면 안됨.
#     A = A[:idx] + A[idx + len_b :]

#     len_a = len(A)

# print(A)

while B in A:
    f = A.find(B)
    A = A[:f] + A[f+len(B):]

print(A)
        