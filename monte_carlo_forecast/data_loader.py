# data_loader.py


import yfinance as yf
import pandas as pd

class DataLoader:
    '''
    This class fetches historical financial data of a company for a range of time.
    '''
    
    def __init__(self, asset, hist_start_date, hist_end_date):
        '''
        Initialize the company symbol, start date, and end date of the historical data
        '''
        self.asset = asset
        self.hist_start_date = hist_start_date
        self.hist_end_date = hist_end_date
        
    def data_download(self):
        '''
        this function downloads the historical data of the asset for the specified range by using yf.download(symbol,...).
        yf.download() allows the downloading data for multiple assets
        '''
        dataframe = yf.download(self.asset, start = self.hist_start_date , end = self.hist_end_date)
        return dataframe
    
    def data_history(self):
        '''
        this function downloads the historical data of the asset for the specified range by using yf.Ticker(symbol).history(...).
        This allows the downloading data for single asset only the additional control over process.
        '''
        ticker = yf.Ticker(self.asset)
        dataframe = ticker.history(start = self.start_date , end = self.hist_end_date, auto_adjust=False)
        return dataframe