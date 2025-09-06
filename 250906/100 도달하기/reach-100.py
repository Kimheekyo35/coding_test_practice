n=int(input())
arr=[]
arr.append(1)
arr.append(n)

for i in range(2,100):
    a=arr[i-1]+arr[i-2]
    arr.append(a)
    if a>=100:
        break

for elem in arr:
    print(elem, end=' ')
