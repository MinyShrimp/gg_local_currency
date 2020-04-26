import requests
from flask import Flask, request, jsonify, render_template
from flask_restful import Api, reqparse
from pprint import pprint

from module.db import DB

app = Flask(__name__)
# api_key = "f7d6fedb7da8439f868b7a4730734ce8"
db = DB()

old_addr        = ''
old_cmpnm_nm    = ''
old_indutype_nm = ''

@app.route('/getlist/<page>', methods = ["POST", "GET"])
def get_data(page):
    try:
        global old_addr
        global old_cmpnm_nm
        global old_indutype_nm

        if request.method == 'POST':
            # 주소
            addr = request.form['REFINE_LOTNO_ADDR'] if request.form['REFINE_LOTNO_ADDR'] else ''
            old_addr = addr
            
            # 상호명
            cmpnm_nm = request.form['CMPNM_NM'] if request.form['CMPNM_NM'] else ''
            old_cmpnm_nm = cmpnm_nm

            # 업종명
            indutype_nm = request.form['INDUTYPE_NM'] if request.form['INDUTYPE_NM'] else ''
            old_indutype_nm = indutype_nm

        elif request.method == 'GET':
            pass
        
        data, count = db.get_datas(old_cmpnm_nm, old_indutype_nm, old_addr, page)

        return render_template('lists.html', 
            data = data,
            page = int(page),
            len_page = int(count/20+1),
            enumerate=enumerate, 
            int=int
        ), 200
    except Exception as e:
        print (e, old_cmpnm_nm, old_indutype_nm)
        return render_template('lists.html', 
            data = [],
            page = 1,
            len_page = 1,
            enumerate=enumerate, 
            int=int
        ), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)