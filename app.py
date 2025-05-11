from flask import Flask, request, jsonify
from pyngrok import ngrok
import requests
import datetime
import config

app = Flask(__name__)

# 启动 ngrok 并打印公网地址
public_url = ngrok.connect(5000)
print(f" * Ngrok tunnel running at: {public_url}")

# 发送消息到 Telegram 的函数
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': config.TELEGRAM_CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    print("Telegram 返回状态码:", response.status_code)

# 接收 TradingView Webhook 的路由
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("收到信号:", data)

    symbol = data.get('ticker', '未知')
    signal = data.get('signal', '无')
    price = data.get('price', 'N/A')
    strategy = data.get('strategy_name', 'Unnamed')
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"📢 [TradingView 信号提醒]\n时间: {time_now}\n标的: {symbol}\n信号: {signal}\n价格: {price}\n策略: {strategy}"
    send_telegram_message(message)

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
