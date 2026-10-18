n = int(input())
satisfied = True

for i in range(2,n):
    # 소수가 아님
    if n%i==0:
        satisfied = False

if satisfied:
    print("P")
else:
    print("C")