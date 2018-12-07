from urllib.request import Request, urlopen
import time


signes_astro = ["sagittaire", "scorpion", "balance", "vierge", "lion", "cancer",
                "gemeaux", "taureau", "belier", "poissons", "verseau", "capricorne"]
fields = ["Humeur:", "Argent:", "Loisirs:", "Amour:", "Travail:"]


def getHoroscopeFull():
    total_lst = []

    for signe in signes_astro:
        req = Request('https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/' + signe + '.htm', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = str(webpage)

        prev_index = 0
        index = 0

        etoiles_lst = []

        for field in fields:
            lst = webpage.split(field)
            etoiles_lst.append((field,lst[1][:230].count("hqson")))

        total_lst.append((signe, etoiles_lst))
    return total_lst
