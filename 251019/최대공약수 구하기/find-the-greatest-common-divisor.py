n, m = map(int, input().split())

# Please write your code here.
def comp_num(n):
    num_list = [ i for i in range(1,n+1) if n % i == 0]
    return num_list

def gcd(n,m):
    n_list = comp_num(n)
    m_list = comp_num(m)
    gcd_list = []
    for i in n_list:
        for j in m_list:
            if i == j : gcd_list.append(i)
    return max(gcd_list)

print(gcd(n,m))
