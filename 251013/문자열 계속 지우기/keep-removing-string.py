A = input()
B = input()
import sys
# Please write your code here.
i = 0
# while True:
#     for j in range(len(B)-1):
#         if A[i] + A[i+1] == B[j]+B[j+1]:
#             A = A[:i] + A[i+2:]
#     i += 1
#     if i > (len(A)-2):
#         break

# print(A)


i = 0
while True:
    if i<len(A)-1:
        if B in A[i] + A[i+1]:
            A = A[:i] + A[i+2:]
            i = 0
        i += 1
    else:
        break

    

print(A)

        