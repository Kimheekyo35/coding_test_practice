a, b = map(int,input().split())
num = a
new = 0
# 정수부분 출력 방식
print(f"{a//b}.",end="")

a %= b
for _ in range(20):
    a *= 10
    print(a//b,end="")

    a %= b
    
# for _ in range(20):
#     new = ((num%b)*10)//b
#     print(new,end="")
#     num = (num%b)*10

