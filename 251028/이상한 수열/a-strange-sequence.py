N = int(input())

# Please write your code here.

def num_ser(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return num_ser(n//3) + num_ser(n-1)

print(num_ser(N))