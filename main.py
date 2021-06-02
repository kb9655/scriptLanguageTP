from Station import *
from Pharmacy import *
from Tourspot import *


s="서울역"
findStation(s)

#아래 좌표를 받았다 가정
xPos = 126.981611
yPos = 37.568477
radius = 1000

searchParmacy(xPos, yPos, radius)
searchTourSpot(xPos, yPos, radius)