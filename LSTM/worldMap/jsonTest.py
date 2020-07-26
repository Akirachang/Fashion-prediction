import os
import json

distros_dict = {}

with open('worldMap.json', 'r') as f:
    distros_dict = json.load(f)

with open('usUnemploy.csv', 'w') as f:
    f.write('State,Unemployment'+'\n')
    for distro in distros_dict['features']:
        print(distro['properties']['name'])
        f.write(distro['properties']['name']+','+'0')
        f.write('\n')