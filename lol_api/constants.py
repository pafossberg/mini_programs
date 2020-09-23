import requests
import pprint
import json
response = requests.get("http://ddragon.leagueoflegends.com/cdn/10.19.1/data/en_US/champion.json")

champRawData = json.loads(response.text)
crd = champRawData['data']

pprint.pprint(crd['Neeko'])
