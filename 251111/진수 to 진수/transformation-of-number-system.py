a, b = map(int, input().split())
n = list(input())

n.reverse()
num = 0
for i in range(len(n)):
    num += (a**i)*(int(n[i]))

digit_list = []
while True:
    if num < b:
        digit_list.append(num)
        break
    
    digit_list.append(num%b)
    num //= b

digit_list.reverse()
for d in digit_list:
    print(d,end="")