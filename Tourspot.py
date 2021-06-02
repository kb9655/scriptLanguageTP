import http.client
import urllib

def searchTourSpot(x, y, rad):
    conn = http.client.HTTPConnection("api.visitkorea.or.kr")
    '''
    http://api.visitkorea.or.kr/openapi/service/rest/KorService/locationBasedList?serviceKey=ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId=15&mapX=126.981611&mapY=37.568477&radius=1000&listYN=Y
    '''
    serviceKey = "ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D"
    xPos = str(x) #"127.0965441345503"
    yPos = str(y) #"37.60765568913871"
    radius = str(rad) #"3000"

    conn.request("GET","/openapi/service/rest/KorService/locationBasedList?serviceKey="+serviceKey+"&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId=15&mapX="+xPos+"&mapY="+yPos+"&radius="+radius+"&listYN=Y")
    req = conn.getresponse()

    l = extractTourSpotData(req.read().decode('utf-8'))
    print(l)

def extractTourSpotData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print(strXml)

    d = {}
    l = []
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.iter("item")    # item 엘리먼트 리스트 추출
   #print(itemElements)
    #print("1")

    for item in itemElements:
        addr = item.find("addr1")
        dist = item.find("dist")
        XPos = item.find("mapx")
        YPos = item.find("mapy")
        telno = item.find("tel")  # 전화번호
        title = item.find("title")  # 이름
        if len(title.text) > 0:
            d = {"Name": title.text, "tel": telno.text, "xPos": XPos.text, "yPos": YPos.text, "address": addr.text, "dist": dist.text}
            l.append(d)
    return l