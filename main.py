# main.py


from monte_carlo_forecast.monte_carlo import MonteCarlo
from monte_carlo_forecast.visualization import plot_trajectories
from monte_carlo_forecast.config import Config
from datetime import datetime,timedelta
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    '''
    - the main function that parses the optional arguments using Config class
    - if initial date is specified by the user then we set historical end date to the initial date and historical start date to 500 days before. 
    - if initial date is not specified by the user then we set historical end date and initial date to today's date.
    
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
    price_trajectories = mc.run_monte_carlo()
    plot_trajectories(price_trajectories, asset)

if __name__ == "__main__":
    main()



