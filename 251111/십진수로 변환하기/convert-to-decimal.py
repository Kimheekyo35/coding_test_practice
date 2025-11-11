binary = list(input())
binary.reverse()
# Please write your code here.
num = 0

for i in range(len(binary)):
    num += (2**i) * int(binary[i])

print(num)

