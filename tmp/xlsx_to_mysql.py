import openpyxl
#import sqlite3
import pymysql

if __name__ == "__main__":
    print('Open Xlsx...')
    book = openpyxl.load_workbook('./locals.xlsx')
    sheet = book.worksheets[0]
    print('Open Xlsx Complete')

    cols = ["SIGUN_NM", "CMPNM_NM", "INDUTYPE_NM", "REFINE_ROADNM_ADDR", "REFINE_LOTNO_ADDR", "TELNO", "REFINE_ZIP_CD", "REFINE_WGS84_LAT", "REFINE_WGS84_LOGT"]

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
    print('Connect DB Complete')

    print('Insert DB...')
    _fl = False
    for row in sheet.rows:
        if _fl == True:
            try:
                cur.execute("""INSERT INTO stores (SIGUN_NM, CMPNM_NM, INDUTYPE_NM, REFINE_ROADNM_ADDR, REFINE_LOTNO_ADDR, TELNO, REFINE_ZIP_CD, REFINE_WGS84_LAT, REFINE_WGS84_LOGT) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");""".format(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value, row[7].value, row[8].value))
            except:
                print([ _.value for _ in row ])
        else:
            _fl = True
    db.commit()
    db.close()
    print('Insert DB Complete')