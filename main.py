from flask import Flask, render_template,request, jsonify
from data_collector import bookmark_stock_data, company_price_data,read_bookmark,company_data
import json
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TESTING'] = True



@app.route('/')
def dashboard():

    return  render_template('dashboard.html')

@app.route('/price/<id>', methods=['GET'])
def get_company_price(id):
    # GET request
    if request.method == 'GET':
        data = company_price_data(id)
        return jsonify(data)

@app.route('/wishlist/', methods=['GET'])
def get_company_wishlist():
    # GET request
    if request.method == 'GET':
        data = read_bookmark()
        # print(json.dump(data))
        return json.dumps(data)


@app.route('/data/<id>', methods=['GET'])
def get_company_data(id):
    # GET request
    if request.method == 'GET':
        data = company_data(id)
        return render_template('index.html',company=data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)