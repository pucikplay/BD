import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import random

class Vitter:
    def __init__(self, sample_size):
        self.A = [None] * sample_size
        self.E = [None] * sample_size
        self.n = 0
        self.k = sample_size

    def onGet(self, z):
        if self.n < self.k:
            self.A[self.n] = z[0]
            self.E[self.n] = z[1]
        else:
            if random.random() < (self.k/self.n):
                i = random.randrange(self.k)
                self.A[i] = z[0]
                self.E[i] = z[1]
        self.n += 1

    def getData(self):
        return self.A,self.E


BTC_Ticker = yf.Ticker("BTC-USD")
BTC_Data = BTC_Ticker.history(period="5y")
BTC_Data.plot(y='Open', use_index=True)
plt.xlabel('Date')
plt.ylabel('USD/BTC')
plt.savefig('charts/full.png', dpi=300)
plt.close()

R = Vitter(40)

for date,row in BTC_Data.iterrows():
    R.onGet((date,row['Open']))

A,E = R.getData()

sample = pd.DataFrame(data={'Date': A, 'Open': E})

sample.plot(x='Date',y='Open')
plt.xlabel('Date')
plt.ylabel('USD/BTC')
plt.savefig('charts/sample.png', dpi=300)
plt.close()