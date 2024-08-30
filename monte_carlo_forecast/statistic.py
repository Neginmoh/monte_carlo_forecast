# statistic.py


from monte_carlo_forecast.config import Config
from monte_carlo_forecast.data_loader import DataLoader
import numpy as np
import pandas as pd

class Statistic:
    '''
    this class performs statistical analysis on financial data
    '''
    def __init__(self, asset, hist_start_date, hist_end_date):
        '''
        initializes the attributes and downloads data
        '''

        self.asset = asset
        self.hist_start_date = hist_start_date
        self.hist_end_date = hist_end_date        
        self.metric = Config.METRIC
        self.data_loader_instance = DataLoader(self.asset, self.hist_start_date, self.hist_end_date)
        self.dataframe = self.data_loader_instance.data_download()
        self.end_date_state = self.dataframe[self.metric][-1]
            
    def simple(self):
        '''
        this method calculates the daily return rates for simple returns of the stock prices
        additionally, calculates the standard deviation, mean and variance of the data

        '''
        daily_returns = self.dataframe[self.metric].pct_change().dropna()
        self.expected_return = daily_returns.mean() # average daily returns or the expected return  for the simple returns
        self.volatility = daily_returns.std()
        self.variance = daily_returns.var() # also equals the volatility**2
        return daily_returns
    
    def logarithmic(self):
        '''
        this method calculates the daily return rates for logarithmic returns of the stock prices
        additionally, calculates the standard deviation, mean and variance of the data
        '''
        log_daily_returns = np.log(1 + self.dataframe[self.metric].pct_change().dropna())
        self.expected_return = log_daily_returns.mean() # average daily returns or the expected return  for the simple returns
        self.volatility = log_daily_returns.std()
        self.variance = log_daily_returns.var() # also equals the volatility**2
        
        return log_daily_returns