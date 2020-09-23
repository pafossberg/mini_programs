import requests
import pprint

response = requests.get("https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/wBR0VGadQtX9yFYHKxXo2nEZnSoj-gPXDC645qTY7jamEg?champion=518&queue=420&api_key=RGAPI-275fb248-8185-4f74-9b50-aac36c19425f")


neeko_ranked = [response.json()['matches'][0]['gameId'] for i in response.json()['matches']]


match_info = requests.get("https://euw1.api.riotgames.com/lol/match/v4/matches/4818774490?api_key=RGAPI-275fb248-8185-4f74-9b50-aac36c19425f")

pprint.pprint(match_info.json()['participants'][8]['championId'])

#for i in match_info.json()['participants']]
