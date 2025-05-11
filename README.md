# tradingview-webhook-alert
🔔 TradingView Webhook 到 Telegram 通知系统

通过Flask接收TradingView的Webhook信号，并自动转发到Telegram通知。

## 🌟 功能特点
- 实时接收TradingView策略警报
- 自动转发到Telegram频道/群组
- 支持ngrok内网穿透
- 完整的错误处理机制

## 🛠️ 技术栈
- **Python 3.8+**
- **Flask** (Web服务器)
- **pyngrok** (内网穿透)
- **Telegram Bot API**

## ⚙️ 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/yourusername/tradingview-webhook-alert.git
cd tradingview-webhook-alert
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置你的 Telegram 和 ngrok 信息
创建一个 `config.py` 文件，内容如下：
```python
TELEGRAM_TOKEN = "你的Telegram Bot Token"
TELEGRAM_CHAT_ID = "你的Telegram Chat ID"
NGROK_AUTH_TOKEN = "你的ngrok authtoken（可选）"
```
> ⚠️ 请不要将 `config.py` 上传到公开仓库，请加入 `.gitignore`。

### 4. 启动服务
```bash
python app.py
```

ngrok 会自动启动，并生成一个公网地址。将该地址配置到 TradingView 的 Webhook URL 中，例如：
```
https://xxxx.ngrok.io/webhook
```
