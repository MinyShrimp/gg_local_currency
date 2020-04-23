import requests
from flask import Flask, request, jsonify, render_template
from pprint import pprint

app = Flask(__name__)
api_key = "f7d6fedb7da8439f868b7a4730734ce8"
sigun_cd = 41310

@app.route('/getlist', methods = ["POST", "GET"])
def get_data():
    pIndex = 1
    if request.method == 'POST':
        # 지역명
        if request.form['SIGUN_NM']:
            sigun_nm = request.form['SIGUN_NM']

        # 상호명
        if request.form['CMPNM_NM']:
            cmpnm_nm = request.form['CMPNM_NM']

        # 업종명
        if request.form['INDUTYPE_NM']:
            indutype_nm = request.form['INDUTYPE_NM']
    elif request.method == 'GET':
        # 페이지
        if request.args.get('pIndex'):
            pIndex = request.args.get('pIndex')
        
    request_url = "https://openapi.gg.go.kr/RegionMnyFacltStus?KEY={}&Type=json&pIndex={}&pSize=20&SIGUN_CD={}".format(api_key, pIndex, sigun_cd)
    data = requests.get(request_url)
    
    try:
        json_data = data.json()
        return render_template('lists.html', 
            data = json_data['RegionMnyFacltStus'][1]['row'],
            enumerate=enumerate, 
        ), 200
    except KeyError:
        return render_template('lists.html', 
            data = {},
            enumerate=enumerate, 
        ), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)