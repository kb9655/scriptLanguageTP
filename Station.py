import http.client
import urllib

def findStation(s):
    conn = http.client.HTTPConnection("openapi.tago.go.kr")
    #s = '정왕'
    #s=input()
    stationName = urllib.parse.quote(s)
    serviceKey = "ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D"
    conn.request("GET","/openapi/service/SubwayInfoService/getKwrdFndSubwaySttnList?serviceKey="+serviceKey+"&subwayStationName="+stationName)
    req = conn.getresponse()


    #print(req.status,req.reason)
    #print(req.read().decode('utf-8'))

    l = extractStationData(req.read().decode('utf-8'))
    print(l)


def extractStationData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print (strXml)
    d = {}
    l = []
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.iter("item")    # item 엘리먼트 리스트 추출
    print(itemElements)

    for item in itemElements:
        subwayStationId = item.find("subwayStationId")          #id 검색
        subwayStationName = item.find("subwayStationName")     #title 검색
        print(subwayStationId.text)
        print(subwayStationName.text)
        '''
                if len(subwayStationName.text) > 0 :
                    print("ok")
                    return {"ID":subwayStationId.text,"Name":subwayStationName.text} # 사전형식 반환
        '''
        if len(subwayStationName.text) > 0:
            d = {"ID":subwayStationId.text, "Name": subwayStationName.text}
            l.append(d)

    return l


