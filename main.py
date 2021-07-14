import json
import requests

def get_heroes():
    heroes_list = ['Captain America', 'Hulk', 'Thanos']
    response = requests.get("https://superheroapi.com/api/2619421814940190/search/Captain_America")
    response2 = requests.get("https://superheroapi.com/api/2619421814940190/search/Hulk")
    response3 = requests.get("https://superheroapi.com/api/2619421814940190/search/Thanos")

    Captain_America = json.loads(response.text)
    Hulk = json.loads(response2.text)
    Thanos = json.loads(response3.text)
    heroes = []
    heroes.append(Captain_America)
    heroes.append(Hulk)
    heroes.append(Thanos)
    heroes_dict = {}
    for hero in heroes:
        hero_results = hero["results"]
        for hero_dates in hero_results:
            if hero_dates["name"] in heroes_list:
                heroes_dict = {hero_dates["name"]: hero_dates["powerstats"]["intelligence"]}

    super_hero = max(heroes_dict, key=heroes_dict.get)
    print(f'Самый умный супергерой: {super_hero}')

get_heroes()

