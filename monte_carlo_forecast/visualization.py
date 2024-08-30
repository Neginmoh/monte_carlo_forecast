# visualization.py


import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

def plot_trajectories(price_trajectories, asset):
    '''
    this function plots all the possible trajectories predicted by Monte Carlo for the specified asset
    '''
    ticker = yf.Ticker(asset)
    info = ticker.info
    company_name = info['longName']
    plt.figure(figsize=(10, 6))
    plt.plot(price_trajectories.T)
    plt.title(f'Monte Carlo Simulation for Predicting Future Prices of {company_name}')
    plt.xlabel("Forecast Horizon (Days)")
    plt.ylabel("Predicted Prices")
    plt.show()
    



