import requests
import os
import base64

from flask import Flask, request, jsonify, render_template, make_response, send_from_directory, redirect
from Crypto.Cipher import AES
from module.db import DB

app = Flask(__name__)
db = DB()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/.well-known/acme-challenge/<txt>')
def set_ssl(txt):
    if txt == 'loVjT5k1cerC6k35D1j21rWExix-ifbZmWgsLcozlNs' or txt == 'wpNbgc-02DLX2okHZT6WMJXAMK59pvo6CGlQe3ETE8I':
        return txt+".CSLTO52_zs-CfKdIgnsblX01wl2xaZ_tKn7VDhSFx8g"
    else:
        return redirect('/')

@app.route('/static/db/<txt>')
def fuck_off(txt):
    return redirect('/')

@app.route('/getlist/<page>', methods = ["POST", "GET"])
def get_data(page):
    try:
        if request.method == 'POST':
            # 주소
            addr = request.form['REFINE_LOTNO_ADDR'] if request.form['REFINE_LOTNO_ADDR'] else ''
            
            # 상호명
            cmpnm_nm = request.form['CMPNM_NM'] if request.form['CMPNM_NM'] else ''

            # 업종명
            indutype_nm = request.form['INDUTYPE_NM'] if request.form['INDUTYPE_NM'] else ''

        elif request.method == 'GET':
            addr = request.cookies.get('REFINE_LOTNO_ADDR')
            cmpnm_nm = request.cookies.get('CMPNM_NM')
            indutype_nm = request.cookies.get('INDUTYPE_NM')

        data, count = db.get_datas(cmpnm_nm, indutype_nm, addr, page)

        resp = make_response(render_template('lists.html', 
            data = data,
            page = int(page),
            len_page = int(count/20+1),
            cookies = (cmpnm_nm, indutype_nm, addr, page),
            enumerate=enumerate, 
            int=int
        ))

        resp.set_cookie('REFINE_LOTNO_ADDR', addr)
        resp.set_cookie('CMPNM_NM', cmpnm_nm)
        resp.set_cookie('INDUTYPE_NM', indutype_nm)

        return resp, 200

    except Exception as e:
        return render_template('lists.html', 
            data = [],
            page = 1,
            len_page = 1,
            cookies = (),
            enumerate=enumerate, 
            int=int
        ), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=80, debug=True)
    app.run(host='0.0.0.0', port=443, ssl_context=('./.https/.certificate.crt', './.https/.private.key'))