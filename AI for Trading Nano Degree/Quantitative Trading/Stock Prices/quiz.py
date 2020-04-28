import pandas as pd

import quiz_tests


def csv_to_close(csv_filepath, field_names):
    """
    Reads in data from a csv file and produces a DataFrame with close data.

    Parameters
    ----------
    csv_filepath : str
        The name of the csv file to read
    field_names : list of str
        The field names of the field in the csv file

    Returns
    -------
    close : DataFrame
        Close prices for each ticker and date
    """
    price_df = pd.read_csv(csv_filepath, names=field_names)
    return price_df.pivot(index='date', columns='ticker', values='close')


if __name__ == "__main__":
    quiz_tests.test_csv_to_close(csv_to_close)
