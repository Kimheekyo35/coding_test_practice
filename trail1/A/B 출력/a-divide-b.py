a, b = map(int,input().split())
num = a
new = 0
print(f"{a//b}.",end="")

for _ in range(20):
    new = ((num%b)*10)//b
    print(new,end="")
    num = (num%b)*10

