import datetime
from pathlib import Path
import pandas as pd
import pytest

from pfo.market_data import download, Source
import pfo.portfolio as pf

path = (Path.cwd() / "data").resolve()
start_date = datetime.datetime(2014, 12, 31)
end_date = '2020-01-01'


###############################################################################
#                                   TUCKERS                                   #
###############################################################################

tickers_pass_csv = [
    ['TSLA', 'FB'],
    ['AAPL', 'AMD'],
    ['AAPL', 'NKE', 'GOOGL', 'AMZN']
]

tickers_pass_yfinance = [
    ['AAPL'],
    ['AAPL', 'AMD'],
]

tickers_pass_moex = [
    ['SBER', 'GAZP', 'MTSS', 'AFLT', 'MOEX'],
    ['SBER', 'GAZP', 'MTSS', 'UNKN'],
    ['SBER'],
]

###############################################################################
#                                     PARAMS                                  #
###############################################################################

d_pass_csv = [
    {'source': Source.CSV, 'tickers': tickers_pass_csv[2], 'path': path, 'start_date': start_date, 'end_date': end_date},
    {'source': Source.CSV, 'tickers': tickers_pass_csv[1], 'path': path},
]

d_pass_yfinance = [
    {'source': Source.YFINANCE, 'tickers': tickers_pass_yfinance[0]},
    {'source': Source.YFINANCE, 'tickers': tickers_pass_yfinance[1], 'start_date': start_date, 'end_date': end_date},
]

d_pass_moex = [
    {'source': Source.MOEX, 'tickers': tickers_pass_moex[0], 'start_date': start_date, 'end_date': end_date},
    {'source': Source.MOEX, 'tickers': tickers_pass_moex[1], 'start_date': start_date, 'end_date': end_date},
    {'source': Source.MOEX, 'tickers': tickers_pass_moex[2]},
]


###############################################################################
#                                       CSV                                   #
###############################################################################
def test_portfolio_csv_pass_0():
    d = d_pass_csv[0]
    data = download(**d)
    portfolio = pf.Portfolio()
    portfolio.build(data)
    # print(portfolio.data.head())

###############################################################################
#                                      MOEX                                   #
###############################################################################
def test_portfolio_moex_pass_0():
    d = d_pass_moex[0]
    data = download(**d)
    portfolio = pf.Portfolio()
    portfolio.build(data)
    # print(portfolio.data.head())