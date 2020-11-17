import numpy as np
import pandas as pd
from pfo.valuations import cov_matrix, yearly_returns

def variance(cov_matrix, weights):
    return cov_matrix.mul(weights, axis=0).mul(weights, axis=1).sum().sum()

def mc_random_portfolios(data, rfr = 0.01, num_portfolios = 10000, yr_calc_alg = 'year', freq = 252):

    pf_ret = [] # Define an empty array for portfolio returns
    pf_vol = [] # Define an empty array for portfolio volatility
    pf_weights = [] # Define an empty array for asset weights
    pf_sharp_ratio = []  # Define an empty array for Sharp ratio

    num_assets = len(data.columns)
    pf_cvm = cov_matrix(data)
    pf_yearly_returns = yearly_returns(data, type=yr_calc_alg)

    for portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights = weights/np.sum(weights)
        pf_weights.append(weights)
        # Returns are the product of individual expected returns of asset and its weights

        returns = np.dot(weights, pf_yearly_returns)
        pf_ret.append(returns)

        var = variance(pf_cvm, weights) # Portfolio Variance
        daily_volatility = np.sqrt(var) # Daily standard deviation
        volatility = daily_volatility*np.sqrt(freq) # Annual standard deviation = volatility
        pf_vol.append(volatility)

        pf_sharp_ratio.append((returns-rfr)/volatility)

    df_rv = {'Returns': pf_ret, 'Volatility': pf_vol, 'Sharp Ratio': pf_sharp_ratio}

    for counter, symbol in enumerate(data.columns.get_level_values(1), start=0):
        df_rv[symbol + ' weight'] = [w[counter] for w in pf_weights]

    portfolios = pd.DataFrame(df_rv)

    return portfolios
