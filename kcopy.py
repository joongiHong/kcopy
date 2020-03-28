'''

[kcopy]

대부분의 코드에는 주석이 포함되어 있습니다.
Github 문서와 주석을 참고하여 필요한 코드만 살려
경량화 하시기 바랍니다.

'''

# ~~ 0. 임포트 부분 ~~
import requests  # (필수) api 서버와 통신용
import json  # (필수) api 사용시 파싱용
import xml.etree.ElementTree as elemTree  # (필수) api 사용시 파싱용

import openpyxl  # (선택) 엑셀 저장용
import csv  # (선택) csv 저장용

# ~~ 1. 공적 마스크 관련 api ~~
# 본 api는 건강보험심사평가원에서 제공하는 공적 마스크 api를 활용하였습니다.


class mask:
    def store(self, page, perpage):  # 공적 마스크 판매점 목록
        if type(page) != int or type(perpage) != int:
            return("VALUE ERROR")
        if perpage < 500:
            return("VALUE ERROR")
        elif perpage > 5000:
            return("VALUE ERROR")

        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json"  # 판매점 목록 api
        para = {
            "page": page,  # 페이지
            "perpage": perpage  # 페이지 당 표시할 판매점 수
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"  # 헤더 정보
        }

        re = requests.get(url, data=para, headers=headers)  # api 통신
        if int(re.status_code) != 200:
            return("SERVER ERROR")  # 통신 에러시 반환
        js = json.loads(re.text)  # json 저장

        if js['storeInfos'] == []:
            return("NO DATABASE")

        return(js['storeInfos'])  # 반환

    def stock(self, page, perpage):
        if type(page) != int or type(perpage) != int:
            return("VALUE ERROR")
        if perpage < 500:
            return("VALUE ERROR")
        elif perpage > 5000:
            return("VALUE ERROR")

        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/sales/json"  # 판매점 목록 api
        para = {
            "page": page,  # 페이지
            "perpage": perpage  # 페이지 당 표시할 판매점 수
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"  # 헤더 정보
        }

        re = requests.get(url, data=para, headers=headers)  # api 통신
        if int(re.status_code) != 200:
            return("SERVER ERROR")  # 통신 에러시 반환
        js = json.loads(re.text)  # json 저장

        if js['sales'] == []:
            return("NO DATABASE")

        return(js['sales'])  # 반환

    def add_stock(self, address):
        if type(address) != str:
            return("VALUE ERROR")

        # 주소 입력 재고 검색 api
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json"
        para = {
            "address": address
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"  # 헤더 정보
        }

        re = requests.get(url, data=para, headers=headers)  # api 통신
        if int(re.status_code) != 200:
            return("SERVER ERROR")  # 통신 에러시 반환
        js = json.loads(re.text)  # json 저장

        if js['stores'] == []:
            return("NO DATABASE")

        return(js['stores'])  # 반환

    def geo_stock(self, lat, lng, m):
        if type(lat) != int or type(lng) != int or type(m) != int:
            return("VALUE ERROR")
        if 33 > lat or lat > 43:
            return("VALUE ERROR")
        elif 124 > lng or lng > 132:
            return("VALUE ERROR")
        elif 5000 < m:
            return("VALUE ERROR")

        # 위도경도 입력 재고 검색 api
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json"
        para = {
            "Lat": lat,
            "lng": lng,
            "m": m
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"  # 헤더 정보
        }

        re = requests.get(url, data=para, headers=headers)  # api 통신
        if int(re.status_code) != 200:
            return("SERVER ERROR")  # 통신 에러시 반환
        js = json.loads(re.text)  # json 저장

        if js['stores'] == []:
            return("NO DATABASE")

        return(js['stores'])  # 반환
