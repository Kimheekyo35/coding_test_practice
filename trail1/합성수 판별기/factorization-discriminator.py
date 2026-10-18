n = int(input())
satisfy = False
for i in range(2,n):
    if n%i==0:
        satisfy = True

if satisfy:
    print("C")
else:
    print("N")