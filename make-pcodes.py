"""Generate a directory of GeoJSON files named after p-codes
"""

import sys, os, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'input',
    type=argparse.FileType('r'),
    metavar="geojson_file",
    nargs='?',
    default=sys.stdin,
    help="GeoJSON file containing the boundaries and p-codes."
)
parser.add_argument(
    '-d', '--output-dir',
    default=".",
    metavar="dir",
    help="Root of the output directory."
)
parser.add_argument(
    '-c',
    '--country',
    required=True,
    metavar="country_code",
    help="ISO 3166-1 alpha3 country code for the shapes."
)
parser.add_argument(
    '-p',
    '--property',
    required=True,
    metavar="adm_prop",
    help="Property name for the ADM code in the GeoJSON."
)
args = parser.parse_args()

geodata = json.load(args.input)

for feature in geodata['features']:
    if feature.get('type') == 'Feature':
        properties = feature.get('properties')
        adm_code = properties.get(args.property)
        print("Dumping {}".format(adm_code))
        # FIXME - make codes safe
        path = '{}/{}/{}'.format(args.output_dir, args.country, adm_code)
        if not os.path.exists(path):
            os.makedirs(path)
        filename = '{}/shape.json'.format(path)
        with open(filename, 'w') as fp:
            json.dump(feature.get('geometry'), fp)
        
