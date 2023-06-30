from flask import Flask, request, Response
import os.path

app = Flask(__name__)

@app.route('/tweets')
def tweets():
    stock_symbol = request.args.get('ticker') 
    if stock_symbol is None:
        return Response('Please provide a stock symbol', status=400)
    # Return the tweets json for the stock symbol from static/tweets/<stock_symbol>.json.
    # If the file doesn't exist, return a 404 with a helpful error message.
    if os.path.isfile('static/tweets/'+stock_symbol+'.json'):
        with open('static/tweets/'+stock_symbol+'.json') as f:
            return Response(f.read(), mimetype='application/json', status=200)
    else:
        return Response({'msg': f'Ticker {stock_symbol.upper()} does not exist.'}, status=200, mimetype='application/json')