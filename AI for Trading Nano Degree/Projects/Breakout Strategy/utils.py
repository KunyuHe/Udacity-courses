import project_tests
import pandas as pd
import numpy as np
from scipy import stats


def get_high_lows_lookback(high, low, lookback_days):
    """
    Get the highs and lows in a lookback window.

    Parameters
    ----------
    high : DataFrame
        High price for each ticker and date
    low : DataFrame
        Low price for each ticker and date
    lookback_days : int
        The number of days to look back

    Returns
    -------
    lookback_high : DataFrame
        Lookback high price for each ticker and date
    lookback_low : DataFrame
        Lookback low price for each ticker and date
    """

    return (high.shift(1).rolling(window=lookback_days).max(),
            low.shift(1).rolling(window=lookback_days).min())


def get_long_short(close, lookback_high, lookback_low):
    """
    Generate the signals long, short, and do nothing.

    Parameters
    ----------
    close : DataFrame
        Close price for each ticker and date
    lookback_high : DataFrame
        Lookback high price for each ticker and date
    lookback_low : DataFrame
        Lookback low price for each ticker and date

    Returns
    -------
    long_short : DataFrame
        The long, short, and do nothing signals for each ticker and date
    """
    return (close > lookback_high).astype(np.int64) - (close < lookback_low).astype(
        np.int64)


def clear_signals(signals, window_size):
    """
    Clear out signals in a Series of just long or short signals.

    Remove the number of signals down to 1 within the window size time period.

    Parameters
    ----------
    signals : Pandas Series
        The long, short, or do nothing signals
    window_size : int
        The number of days to have a single signal

    Returns
    -------
    signals : Pandas Series
        Signals with the signals removed from the window size
    """
    # Start with buffer of window size
    # This handles the edge case of calculating past_signal in the beginning
    clean_signals = [0] * window_size

    for signal_i, current_signal in enumerate(signals):
        # Check if there was a signal in the past window_size of days
        has_past_signal = bool(
            sum(clean_signals[signal_i:signal_i + window_size]))
        # Use the current signal if there's no past signal, else 0/False
        clean_signals.append(not has_past_signal and current_signal)

    # Remove buffer
    clean_signals = clean_signals[window_size:]

    # Return the signals as a Series of Ints
    return pd.Series(np.array(clean_signals).astype(np.int64), signals.index)


def filter_signals(signal, lookahead_days):
    """
    Filter out signals in a DataFrame.

    Parameters
    ----------
    signal : DataFrame
        The long, short, and do nothing signals for each ticker and date
    lookahead_days : int
        The number of days to look ahead

    Returns
    -------
    filtered_signal : DataFrame
        The filtered long, short, and do nothing signals for each ticker and date
    """
    filtered_long = signal.replace(-1, 0).apply(
        lambda col: clear_signals(col, window_size=lookahead_days), axis=0)
    filtered_short = signal.replace(1, 0).replace(-1, 1).apply(
        lambda col: clear_signals(col, window_size=lookahead_days), axis=0
    )

    return filtered_long - filtered_short


def get_lookahead_prices(close, lookahead_days):
    """
    Get the lookahead prices for `lookahead_days` number of days.

    Parameters
    ----------
    close : DataFrame
        Close price for each ticker and date
    lookahead_days : int
        The number of days to look ahead

    Returns
    -------
    lookahead_prices : DataFrame
        The lookahead prices for each ticker and date
    """

    return close.shift(-1 * lookahead_days)


def get_return_lookahead(close, lookahead_prices):
    """
    Calculate the log returns from the lookahead days to the signal day.

    Parameters
    ----------
    close : DataFrame
        Close price for each ticker and date
    lookahead_prices : DataFrame
        The lookahead prices for each ticker and date

    Returns
    -------
    lookahead_returns : DataFrame
        The lookahead log returns for each ticker and date
    """

    return np.log(lookahead_prices) - np.log(close)


def get_signal_return(signal, lookahead_returns):
    """
    Compute the signal returns.

    Parameters
    ----------
    signal : DataFrame
        The long, short, and do nothing signals for each ticker and date
    lookahead_returns : DataFrame
        The lookahead log returns for each ticker and date

    Returns
    -------
    signal_return : DataFrame
        Signal returns for each ticker and date
    """

    return signal * lookahead_returns


def calculate_kstest(long_short_signal_returns):
    """
    Calculate the KS-Test against the signal returns with a long or short signal.

    Parameters
    ----------
    long_short_signal_returns : DataFrame
        The signal returns which have a signal.
        This DataFrame contains two columns, "ticker" and "signal_return"

    Returns
    -------
    ks_values : Pandas Series
        KS static for all the tickers
    p_values : Pandas Series
        P value for all the tickers
    """
    res = long_short_signal_returns.groupby(['ticker']).signal_return.apply(
        lambda x: stats.kstest(x, cdf='norm', args=(
        long_short_signal_returns.signal_return.mean(),
        long_short_signal_returns.signal_return.std(ddof=0)))
    ).apply(pd.Series)

    return res[0], res[1]


def find_outliers(ks_values, p_values, ks_threshold, pvalue_threshold=0.05):
    """
    Find outlying symbols using KS values and P-values

    Parameters
    ----------
    ks_values : Pandas Series
        KS static for all the tickers
    p_values : Pandas Series
        P value for all the tickers
    ks_threshold : float
        The threshold for the KS statistic
    pvalue_threshold : float
        The threshold for the p-value

    Returns
    -------
    outliers : set of str
        Symbols that are outliers
    """
    return set(ks_values[ks_values > ks_threshold].index.union(
        p_values[p_values < pvalue_threshold].index))


if __name__ == "__main__":
    project_tests.test_get_high_lows_lookback(get_high_lows_lookback)
    project_tests.test_get_long_short(get_long_short)
    project_tests.test_filter_signals(filter_signals)
    project_tests.test_get_lookahead_prices(get_lookahead_prices)
    project_tests.test_get_return_lookahead(get_return_lookahead)
    project_tests.test_get_signal_return(get_signal_return)
    project_tests.test_calculate_kstest(calculate_kstest)
    project_tests.test_find_outliers(find_outliers)