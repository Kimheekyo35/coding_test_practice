secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Promise:
    def __init__ (self,secret_code,meeting_point,time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

promise = Promise(secret_code,meeting_point,time)
print("secret code :",promise.secret_code)
print("meeting point :",promise.meeting_point)
print("time :",promise.time)
