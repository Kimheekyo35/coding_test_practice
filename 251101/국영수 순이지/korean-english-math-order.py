class subject:
    def __init__(self,n,k,e,m):
        self.n, self.k, self.e, self.m = n,k,e,m
    
    def __str__(self):
        return f"{self.n} {self.k} {self.e} {self.m}"
n = int(input())
subject_list = []
for _ in range(n):
    name, korean, english, math = tuple(input().split())
    subject_list.append(subject(name,int(korean),int(english),int(math)))

subject_list.sort(key= lambda subject_item:(-subject_item.k,-subject_item.e,-subject_item.m))

for subject_item in subject_list:
    print(subject_item)