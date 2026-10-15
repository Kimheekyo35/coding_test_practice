n = int(input())
prob = 1
# for i in range(1,11):
#     prob *= i
#     if prob >= n:
#         print(i)
#         break

i = 1
while prob < n:
    prob *= i
    i += 1 #n을 6으로 가정했을 때 i가 4가 되어 넘어가기 때문에 -1해줘야함

print(i-1)
