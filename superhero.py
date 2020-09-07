import requests
import os

heroes = {}

# HULK
result_hulk = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Hulk')
list_result_hulk = result_hulk.json()['results']

for dicts_hulk in list_result_hulk:
  if dicts_hulk['name'] == 'Hulk':
    hulk = dicts_hulk['id']
    intelligence_hulk = dicts_hulk['powerstats']['intelligence']
    heroes[hulk] = int(intelligence_hulk)

# Captain America
result_captain_america = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Captain America')
list_result_captain_america = result_captain_america.json()['results']

for dict_captain_america in list_result_captain_america:
    if dict_captain_america['name'] == 'Captain America':
        captain_america = dict_captain_america['id']
        intelligence_captain_america = dict_captain_america['powerstats']['intelligence']
        heroes[captain_america] = int(intelligence_captain_america)

# Thanos
result_thanos = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Thanos')
list_result_thanos = result_thanos.json()['results']

for dict_list_result_thanos in list_result_thanos:
    if dict_list_result_thanos['name'] == 'Thanos':
        thanos = dict_list_result_thanos['id']
        intelligence_thanos = dict_list_result_thanos['powerstats']['intelligence']
        heroes[thanos] = int(intelligence_thanos)

key_name_hero = list(heroes.keys())
value_intelligence = list(heroes.values())

print(f'Самый умный супергерой - это ID {key_name_hero[value_intelligence.index(max(value_intelligence))]}. Его '
      f'интеллект равен {max(value_intelligence)}.')
