# Please write your code here.

n = int(input())
users= []

class User:
    def __init__ (self,name,address,location):
        self.name = name
        self.address = address
        self.location = location

for _ in range(n):
    name, address, location = tuple(input().split())
    users.append(User(name,address,location))

name_list= []
for i in range(n):
    name_list.append(users[i].name)
revise_name = sorted(name_list)
last_name = revise_name[-1]
idx = name_list.index(last_name)
print("name",users[idx].name)
print("addr",users[idx].address)
print("city",users[idx].location)
