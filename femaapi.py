import json
import requests
from datetime import datetime

BASE_URI = 'https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?$filter={resource}'

#filter=incidentType eq 'Flood' or incidentType eq 'Fire'
#disasters must be a list of "'disasterName'"
def filterByType(disasters):
	filters = []
	for disaster in disasters:
		filters.append('incidentType eq ' + disaster)
	params = ' or '.join(filters)
	return BASE_URI.format(resource=params)
'''
example calls
ge >= disasters newer than 1969
declarationDate gt '1969-04-18T04:00:00.000z'
le <= disasters older than 1969
declarationDate le '1969-04-18T04:00:00.000z'
'''
#declarationDate ge '1969-04-18T00:00:00.000z' and declarationDate le '1969-04-22:00:00.000z'
def filterByDate(fromdate, todate):
	fd = fromdate + 'T00:00:00.000z'
	td = todate + 'T00:00:00.000z'
	params = 'declarationDate ge \'{}\' and declarationDate le \'{}\''.format(fd,td)
	return BASE_URI.format(resource=params)

def filterDateType(fromdate, todate, disasters):
	fd = fromdate + 'T00:00:00.000z'
	td = todate + 'T00:00:00.000z'
	filters = []
	for disaster in disasters:
		filters.append('incidentType eq ' + disaster)
	incidents = ' or '.join(filters)
	dates = 'declarationDate ge \'{}\' and declarationDate le \'{}\''.format(fd,td)
	params = dates + ' and (' + incidents + ')'
	return BASE_URI.format(resource=params)

def getjson(uri):
	result = requests.get(uri)
	if result.status_code != 200:
		print('Status: ', result.status_code, ' Error')
	return result.json()