import requests
from flask import Flask, request, jsonify, render_template
from pprint import pprint

app = Flask(__name__)
api_key = "f7d6fedb7da8439f868b7a4730734ce8"
sigun_cd = 41310

@app.route('/getlist', methods = ["POST", "GET"])
def get_data():
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
        
    request_url = "https://openapi.gg.go.kr/RegionMnyFacltStus?KEY={}&Type=json&pIndex=1&pSize=20&SIGUN_CD={}".format(api_key, sigun_cd)
    data = requests.get(request_url)
    json_data = data.json()
    return render_template('lists.html', 
        data = json_data['RegionMnyFacltStus'][1]['row'],
        enumerate=enumerate, 
    ), 200

@app.route('/map', methods=["GET"])
def get_map():
    return render_template('map.html',
        REFINE_WGS84_LAT=request.args.get('REFINE_WGS84_LAT'),
        REFINE_WGS84_LOGT=request.args.get('REFINE_WGS84_LOGT')
    )

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)