import requests
import json
import datetime

def getWeather():
    DAYS = ["Lundi\t\t", "Mardi\t\t", "Mercredi\t", "Jeudi\t\t", "Vendredi\t", "Samedi\t\t", "Dimanche\t"]

    config = open("config.txt", "r").read()
    for line in config.split("\n"):
        sub = line.split(":")[0]
        if sub == "city_id":
            city_id = line.split(":")[1]
        if sub == "WEATHER_API_KEY":
            WEATHER_API_KEY = line.split(":")[1]
        if sub == "unit_type":
            unit_type = line.split(":")[1]    
            
    r = requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + city_id + '?apikey=' + WEATHER_API_KEY + '&language=fr-fr&details=false&metric=' + unit_type)

    parsed = json.loads(r.text)

    txt = ""
    counter = 0
    
    for forecast in parsed['DailyForecasts']:
        if counter == 0:
            txt += "Aujourd'hui\t"
            counter += 1
        elif counter == 1:
            txt += "Demain\t\t"
            counter += 1
        else:
            txt += DAYS[(datetime.datetime.today().weekday()+counter)%7]
            counter += 1
        txt += "Min: " + str(round(forecast['Temperature']['Minimum']['Value'])) + "°C  " + "Max: " + str(round(forecast['Temperature']['Maximum']['Value'])) + "°C\n"
    return txt[:-1]
