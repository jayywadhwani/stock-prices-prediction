from flask import Flask,render_template,request
from model import *
import yfinance as yf

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def predict():
        try:
            symbol = 'SBIN'
            if request.form.get('input_text_symbol') != 'SBIN':
                  symbol= request.form.get('input_text_symbol')
            if request.form.get('input_text_symbol') == None or request.form.get('input_text_symbol')==  "" or request.form.get('input_text_symbol')==  "NULL":
                  symbol = 'SBIN'
            predicted_value,mseerror,maerror,r2score,crscore,previousClose,todayOpen,dayHigh,dayLow,stock_symbol = analysis(symbol)
            return render_template('index.html',predicted_value=predicted_value,r2score=r2score,mseerror=mseerror,maeerror=maerror,vscore=crscore,Previous_Close=previousClose,Todays_Open=todayOpen,Day_High=dayHigh,Day_Low=dayLow,symbol=symbol.upper(),stock_symbol=stock_symbol)
        except Exception as e:
              return "Plesae Reload the page some error occured!!!"

if __name__ == "__main__":
      app.run(debug=True)