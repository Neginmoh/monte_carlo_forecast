# config.py


import argparse

class Config:
    
    METRIC = 'Adj Close'
    NUM_SIMULATIONS = 1000
    DELTA_DAYS = 500
    DEFAULT_SYMBOL = 'AAPL'
    DEFAULT_FORECAST_HORIZON = 90

    def arg_parser(self):
        '''
        this method parses the optional arguments
        --asset: user can enter the symbol of the targeted company. If not provided, the default value is "AAPL" associated with the Apple Inc.
        --forecast_horizon: user can enter the number of days into the future the predictions will extend. If not provided, the default is 90 days.
        --initial_date: user can enter the initial date which is the date from which the predictions begin as well as the historical end date.
                        if not provided, then default initial date is set to the date that on which the script is run.

        historical start date is set to 500 days before historical end date

        '''
        parser = argparse.ArgumentParser(description="Enter the company symbol, number of days into future, and prediction initial date :")
        parser.add_argument("--asset", 
                            type=str, 
                            default=self.DEFAULT_SYMBOL, 
                            help="Enter the symbol for the targeted asset (default: 'AAPL' Apple Inc.)")
        parser.add_argument("--forecast_horizon", 
                            type=int, 
                            default=self.DEFAULT_FORECAST_HORIZON, 
                            help="Enter the number of days into the future the predictions will extend (default: 90 days)")
        parser.add_argument("--initial_date", 
                            type=str, 
                            # default=datetime.now(), 
                            help="Enter the initial date for the prediction, i.e, end date for historica date (default: today's date)")
        return parser.parse_args()