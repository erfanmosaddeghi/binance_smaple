from flask import Flask, json,render_template,request,redirect,flash,jsonify
from binance.client import Client
from binance.enums import *
from datetime import datetime
import config

app = Flask(__name__)

@app.route('/')
def index():
    try:
        account_info = cli.get_account()
        exchange_info = cli.get_exchange_info()
        exchange_info = exchange_info['symbols']

        context = {
            "account_info": account_info,
            "exchange_info": exchange_info
        }
        return render_template('index.html',context=context)
    except Exception as e:
        return render_template('index.html')
    

@app.route('/buy',methods=['POST'])
def buy():
    asset = request.form['asset']
    count = request.form['count']

    try:
        order = cli.create_order(
        symbol=asset,
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=count)
        flash('Success','success')
    except Exception as e:
        flash(e.message,'error')

    return redirect('/')


@app.route('/history')
def history():
    today = datetime.today()
    historicalData = cli.get_historical_klines('BTCUSDT',KLINE_INTERVAL_15MINUTE, "1 january 2021",today.strftime('%Y %b %d %H:%M'))
    candlestick = []

    for data in historicalData:
        candlestick_data = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        }
        candlestick.append(candlestick_data)

    
    return jsonify(candlestick)



if __name__ == '__main__':
    app.secret_key = b'sagbibu31g943f9woerqu8hg94y28hueobv'
    cli = Client(config.API_KEY,config.API_SECRET)
    app.run(debug=True,host='0.0.0.0')