## **사용된 언어**
|                |                                  |
|----------------|----------------------------------|
| 언어           | Python, Html, Javascript         |
| 툴             | Visual Studio Code               |
| 라이브러리     | Flask, Bootstrap, Jquery, SQLite |
| API            | Kakao Map API, 공공데이터 API    |
| 제작 기간      | 2020-03-23 ~ 진행중              |
| 제작 인원      | 1명                              |
| 도움을 받은 곳 | 구글                             |
| 서비스 한 곳   | -                                |

<br>

## **프로젝트 설명**
### **개요**
최근 전세계적인 코로나 열풍으로 대한민국에서는 모든 국민에게 재난 지원금을 각 지역 화폐로 주고 있다. 또한, 홈페이지에서 사용할 수 있는 곳을 알려주며 이를 핸드폰으로 알려주면서 사용할 수 있도록 유도하기도 했다. 

하지만, 아쉽게도 현재 그 사이트에서는 지역과 가게 이름만 검색할 수 있으며 업종과 지도 보기가 현재 제공하지 않아서 불편함이 있었다.

그래서 카카오맵 API와 경기지역화폐 API를 통해 이를 구현함으로써 좀더 편리하게 검색할 수 있도록, 또한 REST에 대한 이해도를 올리기 위해서 이 프로젝트를 진행하게 되었다.

### **새로 배운점**
- [Kakao Map API](https://apis.map.kakao.com/)
- [경기지역화폐 API](https://data.gg.go.kr/portal/data/service/selectServicePage.do?infId=3NPA52LBMO36CQEQ1GMY28894927&infSeq=1)
- SQLite

### **아쉬운 점**
진행중

<br>

## **Files**
- app.py
- /templates/
    - index.html
        - 처음 접속 시 보여주는 페이지
    - lists.html
        - 리스트를 뿌려주는 페이지
- /static/
    - /css/
        - 스타일 시트 폴더
    - /img/
        - 이미지 폴더
    - /db/
        - SQLite Database 폴더
    - /js/
        - getdata.js
            - 데이터 검색
- /module/
    - db.py
        - SQLite Database Control Class
- /tmp/
    - xlsx_to_sqlite.py
        - 경기지역화폐 데이터 시트를 SQLite로 Insert 해주는 파일