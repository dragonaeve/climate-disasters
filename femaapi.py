import json
import requests
from datetime import datetime

BASE_URI = 'https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?$filter={resource}'

def getjson(uri):
	result = requests.get(uri)
	if result.status_code != 200:
		print('Status: ', result.status_code, ' Error')
	return result.json()

#create incidentType filter string
def parseType(disasters):
	filters = []
	for disaster in disasters:
		filters.append('incidentType eq ' + disaster)
	return ' or '.join(filters)

#filter=incidentType eq 'Flood' or incidentType eq 'Fire'
#disasters must be a list of "'disasterName'"
def filterByType(disasters):
	params = parseType(disasters)
	return getjson(BASE_URI.format(resource=params))

#create date range filter string
def parseDates(fromdate, todate):
	fd = fromdate + 'T00:00:00.000z'
	td = todate + 'T00:00:00.000z'
	return 'declarationDate ge \'{}\' and declarationDate le \'{}\''.format(fd,td)

#ge >= disasters newer than
#le <= disasters older than 1969
#declarationDate ge '1969-04-18T00:00:00.000z' and declarationDate le '1969-04-22:00:00.000z'
def filterByDate(fromdate, todate):
	params = parseDates(fromdate, todate)
	return getjson(BASE_URI.format(resource=params))

def filterDateType(fromdate, todate, disasters):
	incidents = parseType(disasters)
	dates = parseDates(fromdate, todate)
	params = dates + ' and (' + incidents + ')'
	return getjson(BASE_URI.format(resource=params))