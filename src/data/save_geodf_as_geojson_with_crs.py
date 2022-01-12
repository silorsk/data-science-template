import geojson
import json

def save_geodf_as_geojson_with_crs(geodf, crs, filename):
    geojson_string = geodf.to_json()
    res = json.loads(geojson_string)
    res['crs'] = {"type":"name","properties":{"name":crs}}
    with open(filename, 'w') as fp:
        geojson.dump(res, fp)