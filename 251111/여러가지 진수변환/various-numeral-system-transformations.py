N, B = map(int, input().split())

digit_list = []

while True:
    if N < 2:
        digit_list.append(N)
        break
    
    digit_list.append(N%B)
    N //= B

digit_list.reverse()
for d in digit_list:
    print(d,end="")