n, m = map(int, input().split())

# Please write your code here.

def lcm(n,m):
    min_val = min(n,m)
    gcd = 0
    result = 0
    for i in range(1,min_val+1):
        if n % i == 0 and m % i == 0:
            gcd = i
    
    result = gcd * (n//gcd) * (m//gcd)
    
    print(result)

lcm(n,m)