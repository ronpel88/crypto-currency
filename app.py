import helpers
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   bitcoin_price = helpers.get_bitcoin_price()
   return render_template('index.html', bitcoin_price=bitcoin_price)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')