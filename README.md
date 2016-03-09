# p-coder
Python script to generate a directory of shape files based on p-codes.

Use this script together with the _shp2geojson_ tool from the [GDAL](http://www.gdal.org/) library to convert an ArcGIS shapefile to a directory of individual files that a browser-side script (or similar) can download on demand, from directories named after p-codes (geographical codes).  Example:

```
shp2geojson myshapefile-shp.zip | python make-pcodes.py -c NPL -p REG_CODE -d /var/share/p-codes
```

# Usage

```
usage: make-pcodes.py [-h] [-d dir] -c country_code -p adm_prop [geojson_file]

positional arguments:
  geojson_file          GeoJSON file containing the boundaries and p-codes.

optional arguments:
  -h, --help            show this help message and exit
  -d dir, --output-dir dir
                        Root of the output directory.
  -c country_code, --country country_code
                        ISO 3166-1 alpha3 country code for the shapes.
  -p adm_prop, --property adm_prop
                        Property name for the ADM code in the GeoJSON.
```
