# main.py


from monte_carlo_forecast.monte_carlo import MonteCarlo
from monte_carlo_forecast.visualization import Plotter
from monte_carlo_forecast.config import Config
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    '''
    The main function that:
    - Parses the optional arguments using Config class, e.g, asset, forecast_horizon, initial_date.
        - if initial date is specified by the user then we set historical end date to the initial date and historical start date to 500 days before. 
        - if initial date is not specified by the user then we set historical end date and initial date to today's date.
    - Runs inference
    - Generates a graph that includes a plot of Monte Carlo trajectories and a histogram of the final day's prices, with annotations for VaR, CVaR, mean losses, and prices.
   
    '''
    config = Config()
    args = config.arg_parser()

    if args.initial_date:
        initial_date = args.initial_date
        initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
    else:
        initial_date = datetime.now()

    hist_end_date = initial_date
    hist_start_date = hist_end_date - timedelta(days=Config.DELTA_DAYS)

    print('hist_start_date', hist_start_date)
    print('initial_date', initial_date)

    asset = args.asset
    forecast_horizon = args.forecast_horizon

    mc = MonteCarlo(asset, forecast_horizon ,hist_start_date, hist_end_date)
    mc.run_inference()

    plotter = Plotter(mc, asset)
    plotter.plot_both() # if both plots are needed, if not run plotter.plot_trajectories() or plotter.plot_histogram()
    plt.show()

if __name__ == "__main__":
    main()



