n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def check_part(a,b):

    for i in range(n1-n2+1):
        list_a = a[i:(i+n2)]
        
        if list_a == b:
            return True


if check_part(a,b):
    print("Yes")
else:
    print("No")
