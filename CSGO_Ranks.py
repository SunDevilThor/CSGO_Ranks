# CSGO_Ranks Table Webscraping
# Firefox > Developer Menu > Network > XHR > Look for JSON data with high amount of KB
# Get URL and open up in a new tab
# Copy/paste URL 

import json
import requests
import pandas as pd

url = 'https://cdn1.api.esl.tv/csgo/worldranking/team/list'

r = requests.get(url)

json_data = r.json()

print(json_data)