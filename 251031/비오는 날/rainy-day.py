class Weather:
    def __init__ (self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
weather_list = [Weather(date, day, weather) for date, day, weather in arr]

idx_list = []
for i,text in enumerate(weather_list):
    if text.weather == "Rain":
        idx_list.append(i)

fix_idx = min(idx_list)
for idx in idx_list:
    if weather_list[fix_idx].date > weather_list[idx].date:
        fix_idx = idx
    
print(weather_list[fix_idx].date,weather_list[fix_idx].day,weather_list[fix_idx].weather)

    
