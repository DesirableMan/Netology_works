<<<<<<< HEAD
import requests
import json


def get_heroes():
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

    for hero in heroes_list:
        hero_dict = json.loads(requests.get(url + hero).content)
        intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

    return intelligence_dict

print(get_heroes())

def most_intelligence():
    return max(get_heroes(), key=get_heroes().get)

print(f'Cамый умный супергерой - {most_intelligence()}')
=======
import requests
import json


def get_heroes():
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

    for hero in heroes_list:
        hero_dict = json.loads(requests.get(url + hero).content)
        intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

    return intelligence_dict

print(get_heroes())

def most_intelligence():
    return max(get_heroes(), key=get_heroes().get)

print(f'Cамый умный супергерой - {most_intelligence()}')
>>>>>>> refs/remotes/origin/main
