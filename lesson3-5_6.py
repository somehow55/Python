# 크롤링을 하기 위해서는 남들이 만들어 놓은 라이브러리를 사용해야 한다. 이것을 파이썬에서는 '패키지'라고 한다.
# 즉, 패키지 설치 = 외부 라이브러리 설치


### 3-6 ↓↓↓↓↓↓↓↓


import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows=rjson['RealtimeCityAir']['row']

for row in rows:
    # print(row)

    gu_name = row['MSRSTE_NM']
    gu_mise = row['IDEX_MVL']

    # print(gu_name, gu_mise)

    if gu_mise < 55:
        print(gu_name, gu_mise)

# print(rows)