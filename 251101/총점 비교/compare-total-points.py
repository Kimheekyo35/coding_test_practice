n = int(input())
# Please write your code here.

class Subject:
    def __init__ (self, name, sub1, sub2, sub3):
        self.name, self.sub1, self.sub2, self.sub3 = name, sub1, sub2, sub3
    def __str__ (self):
        return f"{self.name} {self.sub1} {self.sub2} {self.sub3}"

subject_list = []
for _ in range(n):
    name, score1, score2, score3 = tuple(input().split())
    subject_list.append(Subject(name,int(score1),int(score2),int(score3)))

subject_list.sort(key= lambda x: (x.sub1 + x.sub2 + x.sub3))

for i in subject_list: print(i)
