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


min_idx = ord("a")
for i in range(n):
    if ord(users[i].name[0]) >= min_idx:
        max_idx = i   
    
print("name",users[max_idx].name)
print("addr",users[max_idx].address)
print("city",users[max_idx].location)
