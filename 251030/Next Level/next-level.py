class priv():
    def __init__ (self,user='codetree',level=10):
        self.user = user
        self.level = level


user_id , user_lv = tuple(input().split())
origin = priv()
print("user",origin.user,"lv",origin.level)

origin.user = user_id
origin.level = user_lv
print("user",origin.user,"lv",origin.level)
# Please write your code here.
