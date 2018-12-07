from horoscopeFullGet import getHoroscopeFull

counter = 0

horoscope = getHoroscopeFull()

def getHoroscope(counter):
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

for i in range(3):
    counter, txt = getHoroscope(counter)
    print(txt)
