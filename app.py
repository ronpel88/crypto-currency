import helpers
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   current_price = helpers.get_price()
   avg_price = helpers.calc_average()
   return render_template('index.html', avg_price=avg_price, current_price=current_price)
   

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')