# Basic Flask App

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/insider-trading')
def index():
    stock_symbol = request.args.get('ticker')
    url = f'https://fintel.io/insiders?sticker={stock_symbol.lower()}&sinsider=&smin=&smax=&scode=P&scode=S&sfiledate=7&stradedate=7&Search=Search'
    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            'Accept': 'text/html,application/json,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
    html = requests.get(url, headers=headers).content 
    with open('insider_data.html', 'wb') as f:
        f.write(html)
    return html