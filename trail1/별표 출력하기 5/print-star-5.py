n = int(input())

for i in range(n):
    star = ""
    for j in range(n-i):
        star += "*"
    for k in range(n-i):
        print(star,end=" ")
    print()