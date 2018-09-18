import requests
import json


URL = 'http://api.apixu.com/v1/current.json?key=f0019f1bc9844ad797c134031182005'
locs = []
while True:
    n = int(input("if u'd like to know weather by geo-co-s - enter '1', if by city name - enter '2' : "))
    if n == 1:
        while True:
            # for example London : 51.52 -0.11, Kiev : 50.43 30.52
            coord = str(input("coordinates of the city (if u finished, just type 'end') : "))
            if coord != 'end':
                locs.append(coord)
            else:
                break
        break
    elif n == 2:
        while True:
            name = str(input("name of the city (if u finished, just type 'end') : "))
            if name != 'end':
                locs.append(name)
                continue
            else:
                break
        break
    else:
        print("try again (remember, only '1' or '2'!)")

for loc in locs:
    parameters = {"q": loc}
    respond = requests.get(URL, params=parameters)
    city = respond.json()['location']['name']
    country = respond.json()['location']['country']
    temperature = respond.json()['current']['temp_c']
    condition = respond.json()['current']['condition']['text']
    print('In {}({}) the weather is {} and the temperature is {} °C!'.format(city, country, condition, temperature))


