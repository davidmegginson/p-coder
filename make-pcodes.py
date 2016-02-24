import sys
import os
import json

root_dir = '/home/david/p-codes'
country_code_property = 'CNTRY_CODE'
adm_code_property = 'ADMIN3_PCO'

geodata = json.load(sys.stdin)

for feature in geodata['features']:
    if feature.get('type') == 'Feature':
        properties = feature.get('properties')
        #country_code = properties.get(country_code_property)
        country_code = 'MLI'
        adm_code = properties.get(adm_code_property)
        # FIXME - make codes safe
        path = '{}/{}/{}'.format(root_dir, country_code, adm_code)
        if not os.path.exists(path):
            os.makedirs(path)
        filename = '{}/shape.json'.format(path)
        with open(filename, 'w') as fp:
            json.dump(feature.get('geometry'), fp)
        
