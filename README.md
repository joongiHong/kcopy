<p align="center">
    <img src="logo.png" width="300">
    <h1 align="center" style="font-size: 3em;">KCOPY</h1>
    <p align="center">
        <img src="https://img.shields.io/badge/python-v3.7-blue">
        <img src="https://img.shields.io/badge/license-MIT-green">
    </p>
    <p>KCOPY (Information of COVID-19 for Korean with Python)란 <b>대한민국 정부</b>에서 api를 통하여 제공하는 공식 정보를 쉽게 받아보실 수 있도록 제공하는 모듈입니다. 본 모듈은 api 정보를 파이썬으로 쉽게 가공해 사용하실 수 있도록 돕는 모듈로 <b>정부나 질병관리본부(KCDC)와 연관이 없습니다.</b> 본 모듈은 정부와 건강보험평가심사원 등에서 제공하는 api를 사용하며 본 모듈이 직접 제공하는 정부는 없습니다.</p>
</p>

<br/>

## 시작하기

kcopy는 다음과 같은 모듈을 사용하기에 반드시 존재하여야 합니다.

- requests
- json
- elemTree

아래 모듈은 필요시 설치되어야 하는 모듈입니다.

- openpyxl
- csv

위의 모듈들의 설치가 완료되면 본 kcopy의 깃허브 저장소에서 `kcopy.py` 파일을 다운받아 원하는 프로젝트가 있는 폴더에 설치하시면 됩니다.

## 사용하기

kcopy는 다음과 같은 기능을 지원합니다.

- [공적 마스크 판매처, 재고 조회 (mask)](docs/mask.md)

위와 같은 기능들은 모두 클래스로 이루어져 간단하고 손쉽게 사용하실 수 있습니다. 자세한 사용 방법은 각 api의 문서를 참고하십시오.  
참고로 정부의 api 제공 방침 변경에 따라 지원이 되지 않을 수 있습니다. 이점 양해 부탁드립니다.

## 따라하기

kcopy를 활용한 예제는 다음과 같습니다. 사용하기 파트를 통해서도 잘 이해가 되지 않으시거나 kcopy의 모듈이 정상작동 하지 않을 경우 아래의 검증된 코드를 활용하시기 바랍니다.

<details>
    <summary>mask 활용 예제</summary>

    아래 예제는 서울특별시 강남구 대치동에 위치한 공적 마스크 판매점 및 현재 재고 상태를 표시합니다.

    m = mask()
    print(m.add_stock('서울특별시 강남구 대치동'))

    다음과 같이 출력됩니다.

    [{'addr': '서울특별시 강남구 영동대로86길 10 1층 (대치동)', 'code': '11800461', 'created_at': '2020/03/28 20:05:00', 'lat': 37.5078239, 'lng': 127.0649277, 'name': '메디칼희민약국', 'remain_stat': 'empty', 'stock_at': '2020/03/28 10:19:00', 'type': '01'}, ~~ {'addr': '서울특별시 강남구 테헤란로64길 9 지하1층 101호 (대치동, 선릉역대우아이빌)', 'code': '12870099', 'created_at': None, 'lat': 37.5044976, 'lng': 127.051631, 'name': '펜타약국', 'remain_stat': None, 'stock_at': None, 'type': '01'}]

</details>

## 라이선스 보기

본 모듈의 라이선스는 `MIT LICENSE`입니다.  
따라서 본 모듈을 사용한 모든 프로젝트는 아래의 조건을 준수할 경우 배포, 수정, 상업적 이용을 포함한 모든 행위가 허가됩니다.

> 반드시 출처를 표시해야 합니다.  
> 본 프로젝트의 출처는 본 저장소의 url 주소나 Joongi Hong 혹은 홍준기입니다.

또한 본 모듈에 활용된 오픈소스은 다음과 같습니다.

- [Requests](https://2.python-requests.org/en/master/user/intro/#apache2-license)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)

위의 오픈소스를 제공해 주셔서 다시 한번 감사드립니다.

## 문의하기

본 모듈에 관하여 물어보실 내용은 본 저장소의 이슈 레포트를 활용하여 주십시오.

본 모듈의 개발 과정에 대한 문의는 [블로그](joongi0405.tistory.com)를 방문해 주십시오.

본 모듈이 아닌 개인적인 문의나 기타 문의의 경우 아래 이메일 주소를 활용해 주십시오.

- joongi1978@naver.com
- joongi2006@kakao.com
