from skyfield.api import load, wgs84, EarthSatellite

# print('loaded',len(satellites),'satellites')
ts = load.timescale()
t = ts.now()
line1 = '1 25544U 98067A   22113.52489120  .00011770  00000+0  21220-3 0  9995'
line2 = '2 25544  51.6421 247.3034 0005299  49.4166  72.3404 15.50220861336708'
satellite = EarthSatellite(line1, line2, 'ISS zarya', ts)
# print(satellite.epoch.utc_jpl())
geocentric = satellite.at(t)
# print(geocentric.position.km)
# lat, lon = wgs84.latlon_of(geocentric)
# print('Latitude:', lat)
# print('Longitude:', lon)
position = wgs84.geographic_position_of(geocentric)
lat = position.latitude.degrees
lon = position.longitude.degrees
elevation_km = position.elevation.km
print('Latitude:', lat)
print('Longitude:', lon)
print('Elevation:', elevation_km)
bluffton = wgs84.latlon(lat, lon)
dif = satellite-bluffton
topcentric = dif.at(t)
# print('topocentric position', topcentric.position.km)
alt, az, distance = topcentric.altaz()

# if alt.degrees > 0:
#     print('The ISS is above the horizon')

# print('Altitude:', alt)
# print('Azimuth:', az)
# print('Distance: {:.1f} km'.format(distance.km))
