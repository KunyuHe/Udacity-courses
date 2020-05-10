import quiz_tests


def calculate_returns(close):
    """
    Compute returns for each ticker and date in close.

    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """

    return (close - close.shift(1)) / close.shift(1)


if __name__ == "__main__":
    quiz_tests.test_calculate_returns(calculate_returns)
