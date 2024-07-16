import csv
import requests
from fuzzywuzzy import fuzz
import difflib

base_url = 'https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{}/?apiKey=0d2695b4-a1a9-45c5-aafa-123126078681'


values = []
with open('DFI.csv', 'r', encoding= 'utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if len(row) >= 2:
            values.append((row[0], row[1]))

for oname, cui in values:

    search_url = base_url.format(cui)


    response = requests.get(search_url)


    if response.status_code == 200:
        data = response.json()
        if 'result' in data and 'name' in data['result']:
            name = data['result']['name']
            v= name.lower()
            x= oname.lower()
            similarity = fuzz.ratio(x, v)
            print(f": {oname} | UMLS: {name} | CUI: {cui} | Similarity: {similarity}")
        else:
            print(f"Unable to retrieve the 'name' value for CUI: {cui}")
    else:
        print(f"Error occurred while retrieving data for CUI: {cui}")
