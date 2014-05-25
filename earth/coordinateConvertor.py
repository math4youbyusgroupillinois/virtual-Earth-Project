   # ---------------------------------------------------------------
   # Coordinate Convertor -2014 
   # Sampath Vijayaragavan

   # This module handles conversion from ECEF to LLA and LLA to ECEF
   # for WGS84 model with Earth-centered and Earth-fixed
   # ----------------------------------------------------------------


from math import *

def cbrt(x):
    if x >= 0: 
        return pow(x, 1.0/3.0)
    else:
        return -pow(abs(x), 1.0/3.0)

# Constants defined by the World Geodetic System 1984 (WGS84)
a = 6378.137
b = 6356.7523142
esq = 6.69437999014 * 0.001
e1sq = 6.73949674228 * 0.001
f = 1 / 298.257223563


def geodetic2ecef(lati, longi, alt):
    # Convert geodetic coordinates to ECEF
    lat = radians(float(lati))
    lon = radians(float(longi))
    xi = sqrt(1 - esq * sin(lat) * sin(lat))
    x = (a / xi + alt) * cos(lat) * cos(lon)
    y = (a / xi + alt) * cos(lat) * sin(lon)
    z = (a / xi * (1 - esq) + alt) * sin(lat)
    x = x * 1000
    y = y * 1000
    z = z * 1000
    cartesianList = [round(x,3),round(y,3),round(z,3)]
    return cartesianList


def ecef2geodetic(x, y, z):
    # Convert ECEF coordinates to geodetic.
    # J. Zhu, "Conversion of Earth-centered Earth-fixed coordinates \
    # to geodetic coordinates," IEEE Transactions on Aerospace and \
    # Electronic Systems, vol. 30, pp. 957-961, 1994.
    r = sqrt(x * x + y * y)
    Esq = a * a - b * b
    F = 54 * b * b * z * z
    G = r * r + (1 - esq) * z * z - esq * Esq
    C = (esq * esq * F * r * r) / (pow(G, 3))
    S = cbrt(1 + C + sqrt(C * C + 2 * C))
    P = F / (3 * pow((S + 1 / S + 1), 2) * G * G)
    Q = sqrt(1 + 2 * esq * esq * P)
    r_0 =  -(P * esq * r) / (1 + Q) + sqrt(0.5 * a * a*(1 + 1.0 / Q) - \
        P * (1 - esq) * z * z / (Q * (1 + Q)) - 0.5 * P * r * r)
    U = sqrt(pow((r - esq * r_0), 2) + z * z)
    V = sqrt(pow((r - esq * r_0), 2) + (1 - esq) * z * z)
    Z_0 = b * b * z / (a * V)
    h = U * (1 - b * b / (a * V))
    lat = atan((z + e1sq * Z_0) / r)
    lon = atan2(y, x)
    xi = sqrt(1 - esq * sin(lat) * sin(lat))
    N = a / xi
    height = (r / cos(radians(lat))) - N
    geodeticList = [degrees(lat), degrees(lon), h]
    return geodeticList


def convertXYZtolatlonalt(x, y, z):
    _radiusEquator = 6378137.0
    _radiusPolar = 6356752.3142

    flattening = (_radiusEquator - _radiusPolar) / _radiusEquator
    _eccentricitySquared = 2.0 * flattening - (flattening * flattening)

    p = sqrt(x * x + y * y)
    theta = atan2(z * _radiusEquator , (p * _radiusPolar))
    # theta = radians(theta)
    eDashSquared = (_radiusEquator * _radiusEquator - _radiusPolar * _radiusPolar) / (_radiusPolar * _radiusPolar)
    sin_theta = sin(theta)
    cos_theta = cos(theta)
    latitude = atan((z + eDashSquared * _radiusPolar * sin_theta * sin_theta * sin_theta) / (p - _eccentricitySquared * _radiusEquator * cos_theta * cos_theta * cos_theta))
    longitude = atan2(y, x)
    sin_latitude = sin(radians(latitude))
    N = _radiusEquator / sqrt(1.0 - _eccentricitySquared * sin_latitude * sin_latitude)
    height = p / cos(radians(latitude)) - N

    latlonaltList = [degrees(latitude), degrees(longitude), float(height)]

