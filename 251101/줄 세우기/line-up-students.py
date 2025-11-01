n = int(input())
# Please write your code here.

class Student:
    def __init__ (self,height,weight,number):
        self.height, self.weight, self.number = height, weight, number
    def __str__ (self):
        return f"{self.height} {self.weight} {self.number}"
student_list = []
for i in range(n):
    height,weight = tuple(map(int,input().split()))
    num = i+1
    student_list.append(Student(height,weight,num))

student_list.sort(key = lambda student:(-student.height,-student.weight, student.number))

for i in student_list: print(i)