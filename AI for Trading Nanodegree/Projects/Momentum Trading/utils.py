import numpy as np
import pandas as pd

import project_tests
from scipy import stats


def resample_prices(close_prices, freq='M'):
    """
    Resample close prices for each ticker at specified frequency.

    Parameters
    ----------
    close_prices : DataFrame
        Close prices for each ticker and date
    freq : str
        What frequency to sample at
        For valid freq choices, see http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases

    Returns
    -------
    prices_resampled : DataFrame
        Resampled prices for each ticker and date
    """

    return close_prices.resample(freq).last()


def compute_log_returns(prices):
    """
    Compute log returns for each ticker.

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date

    Returns
    -------
    log_returns : DataFrame
        Log returns for each ticker and date
    """

    return np.log(prices) - np.log(prices.shift(1))


def shift_returns(returns, shift_n):
    """
    Generate shifted returns

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date
    shift_n : int
        Number of periods to move, can be positive or negative

    Returns
    -------
    shifted_returns : DataFrame
        Shifted returns for each ticker and date
    """

    return returns.shift(shift_n)


def get_top_n(prev_returns, top_n):
    """
    Select the top performing stocks

    Parameters
    ----------
    prev_returns : DataFrame
        Previous shifted returns for each ticker and date
    top_n : int
        The number of top performing stocks to get

    Returns
    -------
    top_stocks : DataFrame
        Top stocks for each ticker and date marked with a 1
    """
    isin_top_n = lambda row: row.index.isin(row.nlargest(top_n).index).astype(
        int)
    res = prev_returns.apply(isin_top_n, axis=1)
    return pd.DataFrame.from_dict(dict(zip(res.index, res.values)),
                                  columns=prev_returns.columns,
                                  orient='index')


def portfolio_returns(df_long, df_short, lookahead_returns, n_stocks):
    """
    Compute expected returns for the portfolio, assuming equal investment in each long/short stock.

    Parameters
    ----------
    df_long : DataFrame
        Top stocks for each ticker and date marked with a 1
    df_short : DataFrame
        Bottom stocks for each ticker and date marked with a 1
    lookahead_returns : DataFrame
        Lookahead returns for each ticker and date
    n_stocks: int
        The number number of stocks chosen for each month

    Returns
    -------
    portfolio_returns : DataFrame
        Expected portfolio returns for each ticker and date
    """

    return (df_long - df_short) * lookahead_returns / n_stocks


def analyze_alpha(expected_portfolio_returns_by_date):
    """
    Perform a t-test with the null hypothesis being that the expected mean return is zero.

    Parameters
    ----------
    expected_portfolio_returns_by_date : Pandas Series
        Expected portfolio returns for each date

    Returns
    -------
    t_value
        T-statistic from t-test
    p_value
        Corresponding p-value
    """
    t, p = stats.ttest_1samp(expected_portfolio_returns_by_date, 0.0)

    return t, p / float(2)


if __name__ == "__main__":
    project_tests.test_resample_prices(resample_prices)
    project_tests.test_compute_log_returns(compute_log_returns)
    project_tests.test_shift_returns(shift_returns)
    project_tests.test_get_top_n(get_top_n)
    project_tests.test_portfolio_returns(portfolio_returns)
    project_tests.test_analyze_alpha(analyze_alpha)
