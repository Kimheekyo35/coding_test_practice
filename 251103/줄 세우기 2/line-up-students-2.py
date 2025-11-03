n = int(input())
# Please write your code here.

class Student:
    def __init__ (self,height,weight,num):
        self.height, self.weight, self.num = height, weight, num
    
    def __str__ (self):
        return f"{self.height} {self.weight} {self.num}"

student_list = []
for i in range(n):
    h,w = tuple(map(int,input().split()))
    student_list.append(Student(h,w,i+1))

student_list.sort(key = lambda x: (x.height, -x.weight))

for i in student_list:
    print(i)