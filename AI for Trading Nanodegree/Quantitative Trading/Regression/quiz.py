import numpy as np
import quiz_tests
from sklearn.linear_model import LinearRegression


def regression_slope_and_intercept(xSeries, ySeries):
    """
    xSeries: pandas series, x variable
    ySeries: pandas series, y variable
    """
    lr = LinearRegression()
    lr.fit(xSeries.values.reshape((-1, 1)), ySeries.values.reshape((-1, 1)))

    return (np.float64(lr.coef_.item()),
            np.float64(lr.intercept_.item()))


if __name__ == "__main__":
    quiz_tests.test_regression_slope_and_intercept(
        regression_slope_and_intercept)
