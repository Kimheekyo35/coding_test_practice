N = int(input())

# Please write your code here.

def print_num1(n):
    if n == 0:
        return
    print_num1(n-1)
    print(n,end =" ")

def print_num2(n):
    if n == 0:
        return 
    print(n,end =" ")
    print_num2(n-1)


print_num2(N)
print_num1(N)
        
    