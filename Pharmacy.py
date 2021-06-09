import http.client
import urllib

def searchParmacy(x, y, rad):
    conn = http.client.HTTPConnection("apis.data.go.kr")
    '''
    /B551182/pharmacyInfoService/getParmacyBasisList?serviceKey=ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D&pageNo=1&numOfRows=10&xPos=127.0965441345503&yPos=37.60765568913871&radius=3000
    '''
    serviceKey = "ZGd8LVSUeBw9CoLQalvZyD5G7FP4z4DNfOdqWV48Tvw4zghiyyvY%2FFc1nH1U7rVRKEyz7PeLM6vq4XAkx31RXg%3D%3D"
    xPos = str(x) #"127.0965441345503"
    yPos = str(y) #"37.60765568913871"
    radius = str(rad)#"3000"

    #conn.request("GET","/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey="+serviceKey+"&pageNo=1&numOfRows=10&xPos=127.0965441345503&yPos=37.60765568913871&radius=3000")
    conn.request("GET","/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey="+serviceKey+"&pageNo=1&numOfRows=10&xPos="+xPos+"&yPos="+yPos+"&radius="+radius)
    req = conn.getresponse()

    l = extractParmacyData(req.read().decode('utf-8'))

    return l


def extractParmacyData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print (strXml)
    d = {}
    l = []
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.iter("item")    # item 엘리먼트 리스트 추출
    #print(itemElements)

    for item in itemElements:
        yadmNm = item.find("yadmNm")#이름
        telno = item.find("telno")#전화번호
        XPos = item.find("XPos")
        YPos = item.find("YPos")
        addr = item.find("addr")
        dist = item.find("distance")

        if len(yadmNm.text) > 0:
            d = {"Name": yadmNm.text, "tel": telno.text, "xPos": XPos.text, "yPos": YPos.text, "address": addr.text, "dist": dist.text}
            l.append(d)

    return l