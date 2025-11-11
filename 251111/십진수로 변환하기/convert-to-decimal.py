binary = input()

# Please write your code here.
num = 0

for i in range(len(binary)):
    int(binary[i])
    num += (2**i) * binary[i]

print(num)