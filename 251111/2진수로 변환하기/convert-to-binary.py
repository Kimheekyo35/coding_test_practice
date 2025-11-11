n = int(input())

# Please write your code here.
n_list = []
while True:
    if n < 2:
        n_list.append(n)
        break
    
    n_list.append(n%2)
    n //= 2

for digit in n_list[::-1]:
    print(digit,end="")