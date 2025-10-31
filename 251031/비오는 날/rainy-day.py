class Weather:
    def __init__ (self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
weather_list = [Weather(date, day, weather) for date, day, weather in arr]

idx_list = []
for i in range(n):
    if weather_list[i].weather == "Rain":
        idx_list.append(i)
min_idx = min(idx_list)
for idx in  idx_list:
    if weather_list[min_idx].date > weather_list[idx].date:
        min_idx = i
print(weather_list[min_idx].date,weather_list[min_idx].day,weather_list[min_idx].weather)