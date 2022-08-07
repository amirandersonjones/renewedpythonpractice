import re


import requests as r


# response = r.get(
#     'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
# print(response.status_code)
# if response.status_code == 200:
#     data = response.json()
# print(data['civilizations'][0]['name'])

# make a function
# make the api call and return a dictionary of civilization names, expansion, army_type
def getEmpireData():
    response = r.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    # start producing our dictionary
    civilizatons = []
    for data in data['civilizations']:
        if data['id']:
            civilizatons.append(
                (data['name'], data['expansion'], data['army_type'], data['team_bonus']))
            print(data['name'], data['expansion'], data['army_type'], data['team_bonus'] )
    return civilizatons


getEmpireData()
# print(data['civilizations'][0]['name'])
