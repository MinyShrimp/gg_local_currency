import sqlite3

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
    
    def __connect(self, name):
        if self.db != None:
            print("이미 연결되어 있습니다! - {}".format(self.db_name))
            raise KeyError
        
        self.db_name = name
        self.db = sqlite3.connect( "{}/{}".format(DB_PATH, name) )
        self.cur = self.db.cursor()
    
    def __close(self):
        if self.db != None:
            self.db.close()
            self.__init()
    
    ##########################################################################################################
    ## public functions
    ##########################################################################################################
    def get_codes(self, nm):
        _is_success = False
        rows = ()
        try:
            self.__connect("Local.db")
            self.cur.execute("select SIGUN_CD from locals where SIGUN_NM like '%{}%'".format(nm))
            rows = self.cur.fetchall()
            _is_success = True
        except:
            print("파일 연결 실패!")
        finally:
            self.__close()
        return rows, _is_success
