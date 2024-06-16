import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from feature_engine.outliers import Winsorizer

def analysis(symbol):
    try:
        stock = yf.Ticker(f'{symbol.upper()}.NS')
        quote = stock.info
        previousClose = float(quote.get('previousClose',0))
        todayOpen = float(quote.get('open',0))
        dayHigh = float(quote.get('dayHigh',0))
        dayLow = float(quote.get('dayLow',0))
        volume = float(quote.get('volume',0))
        stock_name = quote.get('longName',"0")
        data = yf.download(f'{symbol.upper()}.NS')
        df = pd.DataFrame(data)
        pd.options.display.float_format = '{:.2f}'.format
        series_shifted_close = df.Close.shift()
        df['prev_close'] = series_shifted_close
        df.fillna(df.mean(), inplace=True)
        df.drop_duplicates(inplace=True)
        df.drop(['Adj Close'], axis=1, inplace=True)
    
        data = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['Open', 'Close', 'Low', 'High', 'prev_close','Volume']).fit_transform(df)

        xtrain, xtest, ytrain, ytest = train_test_split(df[['Open', 'High', 'Low', 'prev_close','Volume']], df['Close'], test_size=0.3, random_state=42, shuffle=False)

        model = LinearRegression()
        model.fit(xtrain, ytrain)

        ypred = model.predict(np.array([todayOpen, dayHigh, dayLow, previousClose,volume]).reshape(1, -1))
        ypred2 = model.predict(xtest)
        mse_error = mean_squared_error(ytest, ypred2)
        mae_error = mean_absolute_error(ytest, ypred2)
        r2s = r2_score(ytest, ypred2)
        crscore = cross_val_score(model, xtrain, ytrain, cv=5)
        return (np.round(ypred[0], decimals=2), np.round(mse_error, decimals=2), np.round(mae_error, decimals=2), np.round(r2s, decimals=2), np.round(crscore[0], decimals=2), np.round(previousClose, decimals=2), np.round(todayOpen, decimals=2), np.round(dayHigh, decimals=2), np.round(dayLow, decimals=2),stock_name)
    except Exception as e:
        return ('Model error occured')

