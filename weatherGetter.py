import datetime
from weather import Weather, Unit

def getWeather():
    config = open("config.txt", "r").read()
    for line in config.split("\n"):
        sub = line.split(":")[0]
        if sub == "weather_city":
            city = line.split(":")[1]
        if sub == "number_of_forecast":
            num_days_forecast = int(line.split(":")[1])

    weather = Weather(unit = Unit.CELSIUS)

    location = weather.lookup_by_location(city)

    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    forecasts = location.forecast
    forecast_lst = []
    count = 0
    for forecast in forecasts[:num_days_forecast]:
        forecast_lst.append(days[(datetime.datetime.today().weekday()+count)%7] + " " + forecast.date + "\n" + forecast.text + " " +
                            forecast.high + " - " + forecast.low + "°C")
        count+=1

    final = ""
    for txt in forecast_lst:
        final += txt + "\n\n"

    #print(final)
    return final[:-2]


