from coordinateConvertor import *
from math import *
from euclid import *
from omega import *
from cyclops import *

import urllib2
import json
import collections


key = "Atb0uB9GCSOQrXNxZNHZz2PAFO4v3NdevcVAD96gZnlNh8c_K9pCxVKQTvYKshtN"
baseURL = "http://dev.virtualearth.net/REST/v1/Locations"

def getLocationbyPoint(lat, lon):
	global key
	global baseURL

	lati = None
	longi = None
	adminDistrict = None
	countryRegion = None
	address = None
	locality = None

	listInfo = []
	decodedDict = {}
	tempDict = {}

	lat = str(lat)
	lon = str(lon)
	url = baseURL + "/" + lat + "," + lon + "?&key=" + key

	result_num = 0
	i = 0

	if(isMaster()):
		req = urllib2.Request(url)
		try:
			response = urllib2.urlopen(req)
			obj = json.loads(response.read())

		except IOError as e:
			print "Get Location by point: URLError Occured " + str(e)
		else:
			result_num = obj['resourceSets'][0]['estimatedTotal']
			result_num = int(result_num)

			if result_num > 0:
				for i in range(result_num):
					decodedDict = convert(obj['resourceSets'][0]['resources'][i])
					if 'geocodePoints' in decodedDict.keys():
						lati = decodedDict['geocodePoints'][0]['coordinates'][0]
						longi = decodedDict['geocodePoints'][0]['coordinates'][1]
					else:
						lati = ' '
						longi = ' '

					if 'address' in decodedDict.keys():
						if 'adminDistrict' in decodedDict['address'].keys():
							adminDistrict = decodedDict['address']['adminDistrict']
						else:
							adminDistrict = ''

						if 'countryRegion' in decodedDict['address'].keys():
							countryRegion = decodedDict['address']['countryRegion']
						else:
							countryRegion = ''

						if 'locality' in decodedDict['address'].keys():
							locality = decodedDict['address']['locality']
						else:
							locality = ''

						if 'formattedAddress' in decodedDict['address'].keys():
							address = decodedDict['address']['formattedAddress']
						else:
							address = '' 

						listInfo = [lati,longi,adminDistrict,countryRegion,locality, address]
						tempDict[i] = listInfo
					else:
						adminDistrict = ''
						countryRegion = ''
						locality = ''
						address = ''

				# print '---------------Dictionary from getLocationbyPoint-------------------'
				# print tempDict
		finally:
			pass
	else:
		pass

	return tempDict

def getLocationbyQuery(locationQuery):
	global key
	global baseURL
	
	lati = None
	longi = None
	adminDistrict = None
	countryRegion = None
	address = None
	locality = None

	listInfo = []
	decodedDict = {}
	tempDict = {}

	result_num = 0
	i = 0

	locationString = parseString(locationQuery)
	url = baseURL + "/" + locationString + "?&key=" + key
		
	if(isMaster()):
		req = urllib2.Request(url)
		try:
			response = urllib2.urlopen(req)
			obj = json.loads(response.read())

		except IOError as e:
			print "Get Location by point: URLError Occured " + str(e)
		else:
			result_num = obj['resourceSets'][0]['estimatedTotal']
			result_num = int(result_num)

			if result_num > 0:
				for i in range(result_num):
					decodedDict = convert(obj['resourceSets'][0]['resources'][i])
					if 'geocodePoints' in decodedDict.keys():
						lati = decodedDict['geocodePoints'][0]['coordinates'][0]
						longi = decodedDict['geocodePoints'][0]['coordinates'][1]
					else:
						lati = ''
						longi = ''

					if 'address' in decodedDict.keys():
						if 'adminDistrict' in decodedDict['address'].keys():
							adminDistrict = decodedDict['address']['adminDistrict']
						else:
							adminDistrict = ''

						if 'countryRegion' in decodedDict['address'].keys():
							countryRegion = decodedDict['address']['countryRegion']
						else:
							countryRegion = ''

						if 'locality' in decodedDict['address'].keys():
							locality = decodedDict['address']['locality']
						else:
							locality = ''

						if 'formattedAddress' in decodedDict['address'].keys():
							address = decodedDict['address']['formattedAddress']
						else:
							address = ''
					else:
						adminDistrict = ''
						countryRegion = ''
						locality = ''
						address = ''

					listInfo = [lati,longi,adminDistrict,countryRegion,locality, address]
					tempDict[i] = listInfo

				print '---------------------------Dictionary from getLocationbyQuery-----------------------------'
				print tempDict
			

		finally:
			# broadcastCommand('oncitySelected("'+ json.dumps(tempDict) +'", interpol_cam, cam)')
			pass

	else:
		pass

	return tempDict

# ###################################helper functions################################################
def parseString(locQuery):
	locQuery = locQuery.strip()
	locQuery = locQuery.lower()
	if locQuery.find(' '):
		locQuery = locQuery.replace(' ', '%20')

	return locQuery

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
######################################################################################################

# def oncitySelected(responseDict,interpol_cam,cam):
# 	tempList = []

# 	responseDict = json.loads(responseDict)
# 	responseDict = convert(responseDict)

# 	if responseDict:
# 		for key in responseDict.keys():
# 			if key == 0:
# 				tempList = responseDict[key]
# 				lat,lon,district,country,locality,address = tempList
# 		lat = json.loads(lat)
# 		lat = float(lat)
# 		lon = json.loads(lon)
# 		lon = float(lon)
# 		district = district.strip()
# 		countryRegion = countryRegion.strip()
# 		locality = locality.strip()
# 		address = address.strip()

# 		#convert lat-lon-alt to cartesian using coordinate Convertor 
# 		targetPos = geodetic2ecef(lat, lon, 300)
# 		lookatPoint = geodetic2ecef(lat, lon, 0)

# 		# get the old position and orientation
# 		qold = cam.getOrientation()
# 		oldPos = cam.getPosition()
# 		# set the new position and look at the City. Get the new orientation
# 		cam.setPosition(Vector3(float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
# 		cam.lookAt(Vector3(float(lookatPoint[0]), float(lookatPoint[1]), float(lookatPoint[2])), Vector3(0.0, 1.0, 0.0))
# 		qnew = cam.getOrientation()
# 		# Restore the old camera position and orientation
# 		cam.setPosition(Vector3(float(oldPos[0]), float(oldPos[1]), float(oldPos[2])))
# 		cam.setOrientation(qold)

# 		#Use oldPos to get (latstart, longistart) and function arguments to get target (latend,longiend)
# 		geodeticlist = ecef2geodetic(float(oldPos[0]),float(oldPos[1]),float(oldPos[2]))
# 		latstart = float(geodeticlist[0])
# 		longistart = float(geodeticlist[1])

# 		interpol_cam.setTargetPosition(Vector3( float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
# 		interpol_cam.generatecircularOrbit(latstart,longistart,lat,lon)
# 		interpol_cam.setTargetOrientation(qnew)
# 		interpol_cam.startInterpolation()
