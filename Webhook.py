# 完整可运行的 Flask + ngrok 示例项目
# 用于接收 TradingView 的 Webhook 并发送 Telegram 通知
# 注意：你需要先安装 Flask 和 pyngrok：pip install flask pyngrok requests

from flask import Flask, request, jsonify
from pyngrok import ngrok
import requests
import datetime

app = Flask(__name__)

# === Telegram 配置 ===
TELEGRAM_TOKEN = ''  # <-- 替换为你自己的 Bot Token
TELEGRAM_CHAT_ID = ''           # <-- 替换为你的 Chat ID

# 发送消息到 Telegram 的函数
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    print("Telegram 返回状态码:", response.status_code)

# === 接收 TradingView Webhook ===
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("收到信号:", data)

    symbol = data.get('ticker', '未知')
    signal = data.get('signal', '无')
    price = data.get('price', 'N/A')
    strategy = data.get('strategy_name', 'Unnamed')
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"\ud83d\udce2 [TradingView 信号提醒]\n时间: {time_now}\n标的: {symbol}\n信号: {signal}\n价格: {price}\n策略: {strategy}"
    send_telegram_message(message)

    return jsonify({"status": "ok"})

# === 主程序 ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
