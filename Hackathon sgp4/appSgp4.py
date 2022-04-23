from sgp4.api import Satrec, jday
s='1 43948U 19006B   22112.43419757  .00012977  00000+0  27574-3 0  9995'
t='2 43948  98.8279 284.5458 0004496 100.7466 259.4285 15.45189608182267'
satellite=Satrec.twoline2rv(s,t)
jd,fr=jday(2022,4,1,12,0,0)

e,r,v=satellite.sgp4(jd,fr)
print(e)