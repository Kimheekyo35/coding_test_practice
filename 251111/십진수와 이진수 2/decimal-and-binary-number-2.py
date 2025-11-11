N = list(input())

N.reverse()

# 2진수 -> 10진수
num = 0
for i in range(len(N)):
    num += (2**i) * int(N[i])

num *= 17

# 10 진수 -> 2진수
digit_list = []
while True:
    if num < 2:
        digit_list.append(num)
        break
    
    digit_list.append(num%2)
    num //= 2

digit_list.reverse()
for d in digit_list:
    print(d,end="")