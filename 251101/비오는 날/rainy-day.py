n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class forecast:
    def __init__ (self,date,day,weather):
        self.date, self.day, self.weather = date, day, weather

    def __str__ (self):
        return f"{self.date} {self.day} {self.weather}"

forecasts = []

for i in range(n):
    forecast_item = forecast(date[i],day[i],weather[i])
    forecasts.append(forecast_item)

forecasts.sort(key= lambda forecast_item : forecast_item.date)

for i in forecasts:
    if i.weather == "Rain":
        print(i)
        break

    
