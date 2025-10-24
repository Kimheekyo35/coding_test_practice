n = int(input())

# Please write your code here.

def bottom_up(n):
    if n == 0:
        return 
    bottom_up(n-1)
    print(n,end = " ")

def up_bottom(n):
    if n == 0:
        return
    print(n,end = " ")
    up_bottom(n-1)
    
bottom_up(n)
print()
up_bottom(n)
