import cvxpy as cvx
import numpy as np


TRADING_DAYS = 252


def generate_dollar_volume_weights(close, volume):
    """
    Generate dollar volume weights.

    Parameters
    ----------
    close : DataFrame
        Close price for each ticker and date
    volume : str
        Volume for each ticker and date

    Returns
    -------
    dollar_volume_weights : DataFrame
        The dollar volume weights for each ticker and date
    """
    assert close.index.equals(volume.index)
    assert close.columns.equals(volume.columns)

    dollar_volume = close * volume
    return dollar_volume.div(dollar_volume.sum(axis=1), axis=0)


def calculate_dividend_weights(dividends):
    """
    Calculate dividend weights.

    Parameters
    ----------
    dividends : DataFrame
        Dividend for each stock and date

    Returns
    -------
    dividend_weights : DataFrame
        Weights for each stock and date
    """
    dividends_cum = dividends.cumsum()

    return dividends_cum.div(dividends_cum.sum(axis=1), axis=0)


def generate_returns(prices):
    """
    Generate returns for ticker and date.

    Parameters
    ----------
    prices : DataFrame
        Price for each ticker and date

    Returns
    -------
    returns : Dataframe
        The returns for each ticker and date
    """

    return prices / prices.shift(1) - 1


def generate_weighted_returns(returns, weights):
    """
    Generate weighted returns.

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date
    weights : DataFrame
        Weights for each ticker and date

    Returns
    -------
    weighted_returns : DataFrame
        Weighted returns for each ticker and date
    """
    assert returns.index.equals(weights.index)
    assert returns.columns.equals(weights.columns)

    return weights * returns


def calculate_cumulative_returns(returns):
    """
    Calculate cumulative returns.

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date

    Returns
    -------
    cumulative_returns : Pandas Series
        Cumulative returns for each date
    """

    return (1 + returns.sum(axis=1, skipna=False)).cumprod()


def tracking_error(benchmark_returns_by_date, etf_returns_by_date):
    """
    Calculate the tracking error.

    Parameters
    ----------
    benchmark_returns_by_date : Pandas Series
        The benchmark returns for each date
    etf_returns_by_date : Pandas Series
        The ETF returns for each date

    Returns
    -------
    tracking_error : float
        The tracking error
    """
    assert benchmark_returns_by_date.index.equals(etf_returns_by_date.index)

    return np.sqrt(TRADING_DAYS) * np.nanstd(
        etf_returns_by_date - benchmark_returns_by_date, ddof=1)


def get_covariance_returns(returns):
    """
    Calculate covariance matrices.

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date

    Returns
    -------
    returns_covariance  : 2 dimensional Ndarray
        The covariance of the returns
    """
    return np.cov(np.nan_to_num(returns).T)


def get_optimal_weights(covariance_returns, index_weights, scale=2.0):
    """
    Find the optimal weights.

    Parameters
    ----------
    covariance_returns : 2 dimensional Ndarray
        The covariance of the returns
    index_weights : Pandas Series
        Index weights for all tickers at a period in time
    scale : int
        The penalty factor for weights the deviate from the index
    Returns
    -------
    x : 1 dimensional Ndarray
        The solution for x
    """
    assert len(covariance_returns.shape) == 2
    assert len(index_weights.shape) == 1
    assert covariance_returns.shape[0] == covariance_returns.shape[1] == \
           index_weights.shape[0]

    m = covariance_returns.shape[0]
    x = cvx.Variable(m)
    portfolio_var = cvx.quad_form(x, covariance_returns)
    distance_to_index = cvx.norm(x - index_weights, p=2)
    objective = cvx.Minimize(portfolio_var + scale * distance_to_index)
    constraints = [sum(x) == 1, x >= 0]

    problem = cvx.Problem(objective, constraints)
    problem.solve()
    return x.value


def rebalance_portfolio(returns, index_weights, shift_size, chunk_size):
    """
    Get weights for each rebalancing of the portfolio.

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date
    index_weights : DataFrame
        Index weight for each ticker and date
    shift_size : int
        The number of days between each rebalance
    chunk_size : int
        The number of days to look in the past for rebalancing

    Returns
    -------
    all_rebalance_weights  : list of Ndarrays
        The ETF weights for each point they are rebalanced
    """
    assert returns.index.equals(index_weights.index)
    assert returns.columns.equals(index_weights.columns)
    assert shift_size > 0
    assert chunk_size >= 0

    m = returns.shape[0]
    weights = []

    for rebalance_point in range(chunk_size, m, shift_size):
        sub = returns.iloc[rebalance_point - chunk_size:rebalance_point, :]
        P = get_covariance_returns(sub)
        weights.append(
            get_optimal_weights(P, index_weights.iloc[rebalance_point - 1]))

    return weights


def get_portfolio_turnover(all_rebalance_weights, shift_size, rebalance_count,
                           n_trading_days_in_year=252):
    """
    Calculage portfolio turnover.

    Parameters
    ----------
    all_rebalance_weights : list of Ndarrays
        The ETF weights for each point they are rebalanced
    shift_size : int
        The number of days between each rebalance
    rebalance_count : int
        Number of times the portfolio was rebalanced
    n_trading_days_in_year: int
        Number of trading days in a year

    Returns
    -------
    portfolio_turnover  : float
        The portfolio turnover
    """
    assert shift_size > 0
    assert rebalance_count > 0

    weights = np.array(all_rebalance_weights)
    avg_turnover = np.abs(weights[1:, :] - weights[:-1, :]).sum() / float(
        rebalance_count)
    n_rebalance_annual = float(n_trading_days_in_year) / float(shift_size)

    return avg_turnover * n_rebalance_annual


if __name__ == '__main__':
    pass