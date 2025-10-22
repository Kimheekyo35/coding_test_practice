A = input()

# Please write your code here.

def find_chain(n):
    for i in range(len(n)):
        count = 0
        for j in range(0,i):
            if n[j] != n[i]:
                count += 1
            if count == 2:
                return True

if find_chain(A):
    print("Yes")
else:
    print("No")