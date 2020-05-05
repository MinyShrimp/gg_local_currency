#import openpyxl
import threading
import sqlite3
import pymysql
import sys, os

###################################################
## init
###################################################
print('Open SQLite...')
conn = sqlite3.connect('./Local.db')
_cur = conn.cursor()
_cur.execute('SELECT * FROM stores;')
_datas = _cur.fetchall()
print('Open SQLite Complete')

print('Connect DB...')
db = pymysql.connect(
    host= '35.229.221.45',
    port=3306,
    user='root',
    passwd='alsl1203',
    db='Local',
    charset='utf8'
)
cur = db.cursor()

_cur.execute("select count(*) from stores;")
_count = _cur.fetchall()
_count = _count[0][0]
_c = 0

lock = threading.Lock()
print('Connect DB Complete')

print('Insert DB...')
###################################################
## functions
###################################################
def insert_db(datas):
    global db, lock, cur

    for _d in datas:
        try:
            lock.acquire()
            global _c, _count

            cur.execute("""INSERT INTO stores (SIGUN_NM, CMPNM_NM, INDUTYPE_NM, REFINE_ROADNM_ADDR, REFINE_LOTNO_ADDR, TELNO, REFINE_ZIP_CD, REFINE_WGS84_LAT, REFINE_WGS84_LOGT) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");""".format(_d[1], _d[2], _d[3], _d[4], _d[5], _d[6], _d[7], _d[8], _d[9]))

            _c += 1
            print('{} / {} ({}%)'.format(_c, _count, round((_c/_count)*100, 2)), end='\r')
            if _c % 1000 == 0:
                db.commit()
                print('commit! - {}                              '.format(_c))

            lock.release()
            
        except Exception as e:
            #pass
            print(e)

###################################################
## main
###################################################
if __name__ == "__main__":
    ths = []

    for i in range(4):
        try:
            rg = int(_count/4) + 2

            tmp = threading.Thread(target=insert_db, args=(list(_datas[i * rg:min((i + 1) * rg, _count)]), ))
            ths.append(tmp)
            tmp.start()

            print('run insert thread - {}'.format(i))
        except Exception as e:
            print(e, i)

    for t in ths:
        t.join()
    
db.commit()
db.close()
print('Insert DB Complete')