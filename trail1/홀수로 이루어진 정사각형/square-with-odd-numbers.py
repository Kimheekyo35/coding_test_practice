n = int(input())
# k = 11

# for i in range(n):
#     tmp = k
#     for j in range(n):
#         print(tmp,end=" ")
#         tmp += 2
#     k += 2

#     print()

# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
for i in range(n):
    for j in range(n):
        print(i*2+j*2+11,end=" ")
    print()