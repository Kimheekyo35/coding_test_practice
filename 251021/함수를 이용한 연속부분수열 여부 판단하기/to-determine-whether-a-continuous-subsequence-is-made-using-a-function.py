n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def check_part(a,b):
    s_a = ""
    s_b = ""
    
    for i in a:
        s_a += str(i) + " "
    for j in b:
        s_b += str(j) + " "

    if s_b in s_a:
        print("Yes")
    else:
        print("No")

check_part(a,b)