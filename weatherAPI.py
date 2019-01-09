from pprint import pprint
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={559a81a07c3f57f41b1aaf2d0d3382f9}')

pprint(r)
