unlock_code, wire_color, seconds =  tuple(input().split())
seconds = int(seconds)

# Please write your code here.

class bomb:
    def __init__ (self, unlock_code,wire_color,seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

bomb_clear = bomb(unlock_code, wire_color, seconds)

print("code :",bomb_clear.unlock_code)
print("color :",bomb_clear.wire_color)
print("second :",bomb_clear.seconds)