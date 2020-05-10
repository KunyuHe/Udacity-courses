import project_tests
import numpy as np


def generate_positions(prices):
    """
    Generate the following signals:
     - Long 30 share of stock when the price is above 50 dollars
     - Short 10 shares when it's below 20 dollars

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date

    Returns
    -------
    final_positions : DataFrame
        Final positions for each ticker and date
    """
    return (prices > 50).astype(np.int64) * 30 - (prices < 20).astype(np.int64) * 10


def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get

    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    return set(sector[prices.loc[date].nlargest(top_n).index])


if __name__ == "__main__":
    project_tests.test_generate_positions(generate_positions)
    project_tests.test_date_top_industries(date_top_industries)
