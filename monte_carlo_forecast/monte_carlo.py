# monte_carlo.py


from monte_carlo_forecast.statistic import Statistic
from monte_carlo_forecast.config import Config
import numpy as np

class MonteCarlo:
    '''
    this class performs Monte Carlo simulation
    '''
    def __init__(self, asset, forecast_horizon, hist_start_date, hist_end_date):
        '''
        - initializes the attributes.
        - performs statistical analysis of historical data using Statistic class for a period in the past
        - creates an empty matrix for storing simulation results for the future days, where each row stores results for a different simulation \ 
        and each column stores data for specific date
        - intializes the first column of the empty matrix with the price value corresponding to the initial date. 
        - Intial date is the date of the last date that we have looked into its historical data and also initial condition of the monte carlo simulation
        '''
        self.num_simulations = Config.NUM_SIMULATIONS
        self.asset = asset
        self.hist_start_date = hist_start_date
        self.hist_end_date = hist_end_date
        self.stat = Statistic(self.asset, self.hist_start_date, self.hist_end_date)
        self.simple_daily_returns = self.stat.simple()
        self.vol = self.stat.volatility
        self.avg = self.stat.expected_return
        self.forecast_horizon = forecast_horizon
        self.num_simulations = Config.NUM_SIMULATIONS
        self.initial_date_state = self.stat.end_date_state
        self.price_trajectories = np.zeros((self.num_simulations, self.forecast_horizon+1))
        self.price_trajectories[:,0] = self.initial_date_state
    
    def run_monte_carlo(self):
        '''
        - this method runs the monte carlo simulation for self.num_simulations times.
        - in each run we randomly sample self.forecast_horizon number of values from normal distribution with a mean value of 0 and standard deviation of 1.
        - scale these sampled random values with the volatility of the daily returns
        - add these scaled sample random values to the mean value of the daily returns to create random rates
        - perform a cumlative sum of these random rates and add 1 to create random growth rates
        - multiply prices of the initial date by the random growth rates to create a data path or data trajectory
        - store this data path in the i-th row corresponding to i-th simulation
        '''

        for i in range(self.num_simulations):
            rand_rates = self.avg + self.vol * (np.random.normal(0, 1, self.forecast_horizon))
            rand_growths = np.cumprod(1 + rand_rates)
            self.price_trajectories[i, 1:] = self.initial_date_state * rand_growths
        return self.price_trajectories
   