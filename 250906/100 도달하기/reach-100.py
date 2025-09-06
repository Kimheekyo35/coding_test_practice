n=int(input())
arr=[1,n]

i=1
while True:
    i+=1    
    arr.append(arr[i-1]+arr[i-2])
    if arr[i]>100:
        break

for elem in arr:
    print(elem, end=' ')