import http.client
import urllib
from urllib.parse import urlparse
import requests
import json

#s="서울역"
#findStation(s)

#xPos = 126.981611
#yPos = 37.568477
#radius = 1000

#searchParmacy(xPos, yPos, radius)
#searchTourSpot(xPos, yPos, radius)
#3a2cd5484e1ba21401ec8685b0f9f694



#address = '서울 중구 한강대로 405 서울역'
address = '경기도 시흥시 정왕동 2325-12'
keyword = '서울역'


# 
#1
url = 'https://dapi.kakao.com/v2/local/search/keyword.json?&query=' + keyword
result = requests.get(urlparse(url).geturl(), headers={'Authorization': 'KakaoAK 3a2cd5484e1ba21401ec8685b0f9f694'}).json()
print(result)
match_first = result['documents'][0]['address_name']
print(match_first)

#2
'''
url = 'https://dapi.kakao.com/v2/local/search/address.json?&query=' + address
result = requests.get(urlparse(url).geturl(), headers={'Authorization': 'KakaoAK 3a2cd5484e1ba21401ec8685b0f9f694'}).json()
print(result)
match_first = result['documents'][0]['address']
lat = float(match_first['y'])
lng = float(match_first['x'])
print(lat, lng)
'''

#https://apis.map.kakao.com/android/guide/#urlscheme_route
