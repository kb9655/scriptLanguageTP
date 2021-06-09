import http.client
import urllib

def searchTourSpot(x, y, rad, cTId):
    conn = http.client.HTTPConnection("api.visitkorea.or.kr")
    serviceKey = "ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D"
    xPos = str(x) #"127.0965441345503"
    yPos = str(y) #"37.60765568913871"
    radius = str(rad) #"3000"
    contentTypeId = cTId
    conn.request("GET","/openapi/service/rest/KorService/locationBasedList?serviceKey="+serviceKey+"&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId="+contentTypeId+"&mapX="+xPos+"&mapY="+yPos+"&radius="+radius+"&listYN=Y")
    req = conn.getresponse()

    l = extractTourSpotData(req.read().decode('utf-8'))
    #print(l)

    return l

def extractTourSpotData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    dTsd = {}
    lTsd = []
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.iter("item")    # item 엘리먼트 리스트 추출


    for item in itemElements:
        addr = item.find("addr1")
        dist = item.find("dist")
        XPos = item.find("mapx")
        YPos = item.find("mapy")
        telno = item.find("tel")  # 전화번호
        title = item.find("title")  # 이름
        image = item.find("firstimage") # 이미지

        dTsd = {"Name": title.text,"xPos": XPos.text, "yPos": YPos.text, "address": addr.text, "dist": dist.text}
        if image != None:
            dTsd.update(image = image.text)
        if telno != None:
            dTsd.update(telno = telno.text)

        lTsd.append(dTsd)
    return lTsd

def searchTourSpotNumbers(x, y, rad):
    conn = http.client.HTTPConnection("api.visitkorea.or.kr")
    serviceKey = "ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D"
    xPos = str(x)  # "127.0965441345503"
    yPos = str(y)  # "37.60765568913871"
    radius = str(rad)  # "3000"
    l = []

    contentTypeId = '15'
    conn.request("GET","/openapi/service/rest/KorService/locationBasedList?serviceKey=" + serviceKey + "&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId=" + contentTypeId + "&mapX=" + xPos + "&mapY=" + yPos + "&radius=" + radius + "&listYN=N")
    req = conn.getresponse()
    l.append(extractNumberOfTourSpot(req.read().decode('utf-8')))

    contentTypeId = '14'
    conn.request("GET","/openapi/service/rest/KorService/locationBasedList?serviceKey=" + serviceKey + "&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId=" + contentTypeId + "&mapX=" + xPos + "&mapY=" + yPos + "&radius=" + radius + "&listYN=N")
    req = conn.getresponse()
    l.append(extractNumberOfTourSpot(req.read().decode('utf-8')))

    contentTypeId = '12'
    conn.request("GET","/openapi/service/rest/KorService/locationBasedList?serviceKey=" + serviceKey + "&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId=" + contentTypeId + "&mapX=" + xPos + "&mapY=" + yPos + "&radius=" + radius + "&listYN=N")
    req = conn.getresponse()
    l.append(extractNumberOfTourSpot(req.read().decode('utf-8')))

    print(l)
    return l

def extractNumberOfTourSpot(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    num = 0
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.iter("item")    # item 엘리먼트 리스트 추출
    for item in itemElements:
        Cnt = item.find("totalCnt")

    return eval(Cnt.text)
