n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def check_part(a,b):

    for i in range(1,len(a)-1):
        list_a = a[i-1:(i-1)+len(b)]
        
        if list_a == b:
            return True

if check_part(a,b):
    print("Yes")
else:
    print("No")
    