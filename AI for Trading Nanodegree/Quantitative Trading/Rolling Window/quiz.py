import quiz_tests
import pandas as pd
import numpy as np


def calculate_simple_moving_average(rolling_window, close):
    """
    Compute the simple moving average.

    Parameters
    ----------
    rolling_window: int
        Rolling window length
    close : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    simple_moving_average : DataFrame
        Simple moving average for each ticker and date
    """
    return close.rolling(window=rolling_window).mean()


def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.

    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.

    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less
        relative to more recent terms.

    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.

    """
    logreturns = np.log(prices) - np.log(prices.shift(1))
    return np.sqrt((logreturns ** 2).ewm(alpha=1 - l).mean()).iloc[-1]


if __name__== "__main__":
    quiz_tests.test_calculate_simple_moving_average(
        calculate_simple_moving_average)