import json
from shapely.geometry import Polygon

#takes json of all US counties and finds min/max lat/long
#poly.bounds = (minX, minY, maxX, maxY)

file = open('gz_2010_us_050_00_500k.json', 'r', encoding="ISO-8859-1")
source = json.load(file)
features = source['features']
for feature in features:
	if feature['geometry']['type'] == "MultiPolygon":
		poly = Polygon(feature['geometry']['coordinates'][0][0])
	else:
		poly = Polygon(feature['geometry']['coordinates'][0])
	print(poly.bounds)