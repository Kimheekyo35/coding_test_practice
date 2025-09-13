arr=list(map(int,input().split()))


under_500_list=[i for i in arr if i<500]
over_500_list=[i for i in arr if i>500]



print(max(under_500_list), min(over_500_list))
    