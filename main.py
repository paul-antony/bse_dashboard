from flask import Flask, render_template
from data_collector import bookmark_stock_data


app = Flask(__name__)


@app.route('/')
def dashboard():

    data = bookmark_stock_data()
    return  render_template('index.html',data=data)

if __name__ == '__main__':
    app.run()