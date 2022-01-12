import geopandas as gpd

import nvdbapiv3 as nvdb
from nvdbapiv3 import nvdb2geojson

from data import save_geodf_as_geojson_with_crs as savedf


data = nvdb.nvdbFagdata(482) # Trafikkregistreringsstasjoner

# (Status=Operativ OR Status=Midlertidig ute av drift) AND Trafikantgruppe=Sykkel
data.filter({"egenskap": "(5201=7081 OR 5201=12987) AND 9293=12993"})

data_geo = nvdb2geojson.fagdata2geojson(data)
geodf = gpd.GeoDataFrame.from_features(data_geo['features'])
geodf.set_crs(epsg=25833)

savedf.save_geodf_as_geojson_with_crs(geodf, "EPSG:25833", 'test.geojson')