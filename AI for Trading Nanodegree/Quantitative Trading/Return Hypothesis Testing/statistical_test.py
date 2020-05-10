import sys

import pandas as pd
import scipy.stats as stats

sys.path.append("../../")
from tests import project_test, assert_output
from collections import OrderedDict

def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    null_hypothesis = 0.0
    t, p = stats.ttest_1samp(net_returns, null_hypothesis)
    # Divde the p-value by 2 to get the results of a one-tailed p-value.
    return round(t, 3), round(p / float(2), 6)


@project_test
def test_analyze_returns(filename='net_returns.csv'):
    """Test run analyze_returns() with net strategy returns from a file."""
    net_returns = pd.Series.from_csv(filename, header=0)
    fn_inputs = {'net_returns': net_returns}
    fn_outputs = OrderedDict([
        (
            '(t, p)',
            (0.760, 0.226606)
        )
    ])

    assert_output(analyze_returns, fn_inputs, fn_outputs)


if __name__ == '__main__':
    test_analyze_returns()
