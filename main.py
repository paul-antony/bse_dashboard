from flask import Flask, render_template,request, jsonify
from data_collector import bookmark_stock_data, company_price_data,read_bookmark
import json

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TESTING'] = True

@app.route('/')
def dashboard():

    data = bookmark_stock_data()
    return  render_template('index.html',data=data)


@app.route('/test')
def test():

    return  render_template('test.html')

@app.route('/price/<id>', methods=['GET'])
def get_company_data(id):
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


if __name__ == '__main__':
    app.run()