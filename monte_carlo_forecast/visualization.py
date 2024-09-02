# visualization.py


import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


class Plotter:
    '''
    This class is used to plot the results.
    It includes methods to plot monte carlo trajectories, final prices histogram or both.

    Args:
        mc (MonteCarlo) : An instance of MonteCarlo class
        asset (str) : The symbol for the company under study    
    '''
    def __init__(self, mc, asset, initial_date, delta_days):
        '''
        It initializes the necessary attributes
        '''
        self.asset = asset
        self.initial_date = initial_date
        self.delta_days = delta_days
        self.price_trajectories = mc.price_trajectories
        self.final_prices = mc.final_prices
        self.VaR = mc.VaR
        self.price_at_VaR = mc.price_at_VaR
        self.CVaR = mc.CVaR
        self.price_at_CVaR = mc.price_at_CVaR
        self.mean_loss = mc.mean_loss
        self.price_at_mean = mc.price_at_mean
        
    def plot_trajectories(self):
        '''
        this function plots all the possible trajectories predicted by Monte Carlo, starting from initial date, for the specified asset
        '''
        
        ticker = yf.Ticker(self.asset)
        info = ticker.info
        company_name = info['longName']
        plt.plot(self.price_trajectories.T, linewidth=0.5)

        min_y, max_y = plt.ylim()
        min_x, max_x = plt.xlim()

        date_y = max_y - 0.15 * (max_y - min_y)
        date_x = min_x + 0.05 * (max_x - min_x)

        plt.text(date_x, date_y, f'Initial Date = {self.initial_date.date()}\n{self.delta_days} days of historical data', fontsize = 6, 
                bbox = dict(facecolor = 'red', alpha = 0.2))

        plt.xlabel("Forecast Horizon (Days)",fontsize=8)
        plt.ylabel("Predicted Prices",fontsize=8)
        plt.title(f'Monte Carlo Simulation for Predicting Future Prices of {company_name}', fontsize=10)

    
    def plot_histogram(self):
        '''
        this function plots a histogram of the prices at the final day.
        The histogram specified the average, VaR, CVaR losses and prices.
        '''
        n, _, _ = plt.hist(self.final_prices, bins=100 , color='blue', edgecolor='darkgrey',alpha =0.6)
        pad = (max(self.final_prices)-min(self.final_prices))*0.1

        # VaR
        plt.axvline(x=self.price_at_VaR, color='red', linestyle='--', linewidth=1)
        plt.axvspan(xmin=0, xmax=self.price_at_VaR, color='red', alpha=0.2)
        plt.annotate(
            'VaR Price',
            xy=(self.price_at_VaR, max(n) * 0.98),
            xytext=((min(self.final_prices) - pad * 0.9), max(n) * 0.98),
            arrowprops=dict(
                edgecolor='red',
                arrowstyle='->'
            ),
            fontsize=6,
            color='red'
        )
        plt.text(
            (min(self.final_prices) - pad * 0.88),
            max(n) * 0.88,
            'VaR Loss\n = {:.2f}'.format(self.VaR),
            fontsize=6,
            color='red'
        )

        # CVaR
        plt.axvline(x=self.price_at_CVaR, color='green', linestyle='--', linewidth=1)
        plt.axvspan(xmin=0, xmax=self.price_at_CVaR, color='green', alpha=0.2)
        plt.annotate(
            'CVaR Price',
            xy=(self.price_at_CVaR, max(n) * 0.70),
            xytext=((min(self.final_prices) - pad * 0.9), max(n) * 0.70),
            arrowprops=dict(
                edgecolor='green',
                arrowstyle='->'
            ),
            fontsize=6,
            color='green',  
        )
        plt.text(
            (min(self.final_prices) - pad * 0.9),
            max(n) * 0.60,
            'CVaR Loss\n = {:.2f}'.format(self.CVaR),
            fontsize=6,
            color='green'
        )

        # mean
        plt.axvline(x=self.price_at_mean, color='black', linestyle='--', linewidth=1)
        plt.annotate(
            'Mean Price',
            xy=(self.price_at_mean, max(n) * 0.90),
            xytext=(self.price_at_mean + pad, max(n) * 0.90),
            arrowprops=dict(
                edgecolor='black',
                arrowstyle='->'
            ),
            fontsize=6,
            color='black',  
        )
        plt.text(
            (self.price_at_mean + pad),
            max(n) * 0.80,
            'Mean Loss\n = {:.2f}'.format(self.mean_loss),
            fontsize=6,
            color='black'
        )

        plt.xlim(min(self.final_prices) - pad, max(self.final_prices) + pad)
        plt.ylim(0, None)
        plt.xlabel('Final Prices',fontsize=8)
        plt.ylabel('Frequency',fontsize=8)
        plt.title('Distribution of Final Prices',fontsize=10)

    def plot_both(self):
        '''
        this function plots both plot_trajectories() and plot_histogram() within a same figure.
        '''
        fig = plt.figure(figsize=(8, 6))
        subplot_size = 0.35 
        top_margin = 0.58
        bottom_margin = 0.1

        left_margin = (1 - subplot_size) / 2
        fig.add_axes([left_margin, top_margin, subplot_size, subplot_size])
        self.plot_trajectories()  

        fig.add_axes([left_margin, bottom_margin, subplot_size, subplot_size])
        self.plot_histogram() 




