var chart = LightweightCharts.createChart(document.getElementById('chart'), {
    width: 850,
    height: 350,
    layout: {
        backgroundColor: '#000000',
        textColor: 'rgba(255, 255, 255, 0.9)',
    },
    grid: {
        vertLines: {
            color: 'rgba(197, 203, 206, 0.5)',
        },
        horzLines: {
            color: 'rgba(197, 203, 206, 0.5)',
        },
    },
    crosshair: {
        mode: LightweightCharts.CrosshairMode.Normal,
    },
    rightPriceScale: {
        borderColor: 'rgba(197, 203, 206, 0.8)',
    },
    timeScale: {
        borderColor: 'rgba(197, 203, 206, 0.8)',
    },
});

var candleSeries = chart.addCandlestickSeries({
    upColor: 'rgba(0, 255, 0, 1)',
    downColor: 'rgba(255, 0, 0, 1)',
    wickDownColor: 'rgba(150, 0, 0, 1)',
    wickUpColor: 'rgba(0, 150, 0, 1)',
});

fetch('http://127.0.0.1:5000/history')
    .then((r) => r.json())
    .then((response) => {
        candleSeries.setData(response);
    });


web = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@kline_15m');

web.onmessage = function(event) {
    var message = JSON.parse(event.data)

    var candlestick = message.k

    candleSeries.update({
        "time": candlestick.t / 1000,
        "open": candlestick.o,
        "high": candlestick.h,
        "low": candlestick.l,
        "close": candlestick.c
    });

}