#import sqlite3
import pymysql
import re

def is_regular(_strs):
    p = re.compile('SELECT|UPDATE|UNION|DELETE|INSERT|WHERE|HAVING|OR|COMMIT', re.I)
    for _ in _strs:
        if p.search(_) != None:
            return False
    else:
        return True

DB_PATH = './static/db'
class DB:
    def __init__(self):
        self.__init()

    def __del__(self):
        self.__close()

    ##########################################################################################################
    ## private functions 
    ##########################################################################################################
    def __init(self):
        self.db = None
        self.db_name = ""
    
    #def __connect(self, name):
    def __connect(self):
        while True:
            if self.db == None:
                #self.db_name = name
                #self.db = sqlite3.connect( "{}/{}".format(DB_PATH, name) )
                self.db = pymysql.connect(
                    host= '35.229.221.45',
                    port=3306,
                    user='root',
                    passwd='alsl1203',
                    db='Local',
                    charset='utf8'
                )
                self.cur = self.db.cursor()

                return True
    
    def __close(self):
        if self.db != None:
            self.db.close()
            self.__init()
    
    ##########################################################################################################
    ## public functions
    ##########################################################################################################
    def get_codes(self, nm):
        _is_success = False
        rows = []
        try:
            #self.__connect("Local.db")
            self.__connect()
            self.cur.execute("select SIGUN_CD from locals where SIGUN_NM like '%{}%'".format(nm))
            rows = self.cur.fetchall()
            _is_success = True
        except:
            print("파일 연결 실패!")
        finally:
            self.__close()
        return rows, _is_success

    def get_datas(self, cmp_nm, induty_nm, addr, page):
        _datas = []
        _count = 0
        if is_regular([cmp_nm, induty_nm, addr]) is False:
            return _datas, _count
        
        try:
            #self.__connect("Local.db")
            self.__connect()
            _limit = (int(page) - 1) * 20
            self.cur.execute("select ID, SIGUN_NM, CMPNM_NM, INDUTYPE_NM, REFINE_LOTNO_ADDR, TELNO, REFINE_WGS84_LAT, REFINE_WGS84_LOGT from stores where CMPNM_NM like '%{}%' and INDUTYPE_NM like '%{}%' and REFINE_LOTNO_ADDR like '%{}%' LIMIT {}, 20".format(cmp_nm, induty_nm, addr, _limit))
            _datas = self.cur.fetchall()

            self.cur.execute("select count(*) from stores where CMPNM_NM like '%{}%' and INDUTYPE_NM like '%{}%' and REFINE_LOTNO_ADDR like '%{}%'".format(cmp_nm, induty_nm, addr))
            _count = self.cur.fetchall()
            _count = _count[0][0]
        except Exception as e:
            print("파일 연결 실패", e)  
        finally:
            self.__close()
        return _datas, _count

if __name__ == "__main__":
    db = DB()
    data = db.get_datas('안양', '', '', 1)
    print(type(data[0]), data[1])