import openpyxl
import sqlite3

if __name__ == "__main__":
    book = openpyxl.load_workbook('./locals.xlsx')
    sheet = book.worksheets[0]
    
    cols = ["SIGUN_NM", "CMPNM_NM", "INDUTYPE_NM", "REFINE_ROADNM_ADDR", "REFINE_LOTNO_ADDR", "TELNO", "REFINE_ZIP_CD", "REFINE_WGS84_LAT", "REFINE_WGS84_LOGT"]

    db = sqlite3.connect( "./Local.db" )
    cur = db.cursor()

    _fl = False
    for row in sheet.rows:
        if _fl == True:
            cur.execute("INSERT INTO stores (SIGUN_NM, CMPNM_NM, INDUTYPE_NM, REFINE_ROADNM_ADDR, REFINE_LOTNO_ADDR, TELNO, REFINE_ZIP_CD, REFINE_WGS84_LAT, REFINE_WGS84_LOGT) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value, row[7].value, row[8].value))
        else:
            _fl = True
    
    db.close()