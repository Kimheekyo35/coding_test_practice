n=int(input())



list_n=map(int,input().split())

new_list=[i for i in list_n if i%2==0]

for i in new_list[::-1]:
    print(i,end=' ')
        