## **사용된 언어**
|                |                                                |
|----------------|------------------------------------------------|
| 언어           | Python, Html, Javascript                       |
| 툴             | Visual Studio Code                             |
| 라이브러리     | Flask, Bootstrap, Jquery, SQLite, MySQL        |
| API            | Naver Map API, Kakao Map API, 공공데이터 API   |
| 제작 기간      | 2020-04-23 ~ 2020-05-02                            |
| 제작 인원      | 1명                                            |
| 도움을 받은 곳 | 구글                                           |
| 서비스 한 곳   | [Google Cloud Platform](https://www.gfind.kr/) |

<br>

## **프로젝트 설명**
### **개요**
최근 전세계적인 코로나 열풍으로 대한민국에서는 모든 국민에게 재난 지원금을 각 지역 화폐로 주고 있다. 또한, 홈페이지에서 사용할 수 있는 곳을 알려주며 이를 핸드폰으로 알려주면서 사용할 수 있도록 유도하기도 했다. 

하지만, 아쉽게도 현재 그 사이트에서는 지역과 가게 이름만 검색할 수 있으며 업종과 지도 보기가 현재 제공하지 않아서 불편함이 있었다.

그래서 카카오맵 API와 경기지역화폐 API를 통해 이를 구현함으로써 좀더 편리하게 검색할 수 있도록, 또한 REST에 대한 이해도를 올리기 위해서 이 프로젝트를 진행하게 되었다.

### **새로 배운점**
- [Naver Map API](https://navermaps.github.io/maps.js.ncp/docs/index.html)
- [Kakao Map API](https://apis.map.kakao.com/)
- [경기지역화폐 API](https://data.gg.go.kr/portal/data/service/selectServicePage.do?infId=3NPA52LBMO36CQEQ1GMY28894927&infSeq=1)
- SQLite => MySQL로 변경 ( 동시 접속을 위함 )
- robots.txt
- https와 ssl 인증
- [도메인 구매](https://www.dotname.co.kr/)

### **아쉬운 점**
진행중

<br>

## **Files**
- /root/
    - app.py
    - robots.txt
- /templates/
    - index.html
        - 처음 접속 시 보여주는 페이지
    - lists.html
        - 리스트를 뿌려주는 페이지
- /static/
    - /css/
        - 스타일 시트 폴더
    - /db/
        - SQLite Database 폴더
        - [2020-04-29 동시 접속 문제로 삭제] : MySQL로 대체
    - /js/
        - getdata.js
            - 데이터 검색
- /module/
    - db.py
        - SQLite Database Control Class
- /tmp/
    - xlsx_to_sqlite.py (삭제됨)
        - 경기지역화폐 데이터 시트를 SQLite로 Insert 해주는 파일
    - xtm.py
        - SQLite 데이터를 MySQL로 Insert 해주는 파일
