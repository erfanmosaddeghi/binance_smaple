web = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@kline_15m');

web.onmessage = function(event) {
    var message = JSON.parse(event.data)
        //console.log(message)
}

//{"e":"trade","E":1612081873929,"s":"BTCUSDT","t":609330793,"p":"33730.24000000","q":"0.04028500","b":4586682826,"a":4586682830,"T":1612081873926,"m":true,"M":true}