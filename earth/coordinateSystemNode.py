from math import *

_radiusEquator = 6378137.0
_radiusPolar = 6356752.3142
flattening = (_radiusEquator - _radiusPolar) / _radiusEquator
_eccentricitySquared = 2.0 * flattening - (flattening * flattening)


def convertlatlonalttoXYZ(latitude,longitude,height):
	global _radiusEquator
	global _radiusPolar
	global _eccentricitySquared

	sin_latitude = sin(radians(latitude))
	cos_latitude = cos(radians(latitude))
	N = _radiusEquator / sqrt( 1.0 - _eccentricitySquared * sin_latitude * sin_latitude)
	X = (N + height) * cos_latitude * cos(radians(longitude))
	Y = (N + height) * cos_latitude * sin(radians(longitude))
	Z = (N * (1-_eccentricitySquared) + height) * sin_latitude
	XYZList = [float(X), float(Y), float(Z)]
	return XYZList


def convertXYZtolatlonalt(x, y, z):
	global _radiusEquator
	global _radiusPolar
	global _eccentricitySquared
	global flattening

	p = sqrt(x * x + y * y)
	theta = atan2(z * _radiusEquator , (p * _radiusPolar))
	theta = radians(theta)
	eDashSquared = (_radiusEquator * _radiusEquator - _radiusPolar * _radiusPolar) / (_radiusPolar * _radiusPolar)
	sin_theta = sin(theta)
	cos_theta = cos(theta)
	latitude = atan((z + eDashSquared * _radiusPolar * sin_theta * sin_theta * sin_theta) / (p - _eccentricitySquared * _radiusEquator * cos_theta * cos_theta * cos_theta))
	longitude = atan2(y, x)
	sin_latitude = sin(radians(latitude))
	N = _radiusEquator / sqrt(1.0 - _eccentricitySquared * sin_latitude * sin_latitude)
	height = p / cos(radians(latitude)) - N

	latlonaltList = [degrees(latitude), degrees(longitude), float(height)]
	return latlonaltList