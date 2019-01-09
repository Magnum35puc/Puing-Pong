from horoscopeFullGet import getHoroscopeFull

def getHoroscope(counter, horoscope):
    text = ""

    horosigne = horoscope[counter]
    text += horosigne[0] + "\n"
    for field in horosigne[1]:
        text += field[0]
        for i in range(field[1]):
            text += "*"
        for i in range(5-field[1]):
            text += " "
        text += "\n"

    counter += 1
    counter %= 12
    return counter, text

def getMyHoro():
    horoscope = getHoroscopeFull()

    config = open("config.txt", "r").read()
    for line in config.split("\n"):
        sub = line.split(":")[0]
        if sub == "horoscope":
            horo = line.split(":")[1].split(",")
    
    counter = 0
    
    toRet = ""
    
    for i in range(12):
        counter, txt = getHoroscope(counter, horoscope)
        if txt.split("\n")[0] in horo:
            toRet += txt
    return toRet
