import cvxpy as cvx
import numpy as np
import quiz_tests


def optimize_twoasset_portfolio(varA, varB, rAB):
    """Create a function that takes in the variance of Stock A, the variance of
    Stock B, and the correlation between Stocks A and B as arguments and returns
    the vector of optimal weights

    Parameters
    ----------
    varA : float
        The variance of Stock A.

    varB : float
        The variance of Stock B.

    rAB : float
        The correlation between Stocks A and B.

    Returns
    -------
    x : np.ndarray
        A 2-element numpy ndarray containing the weights on Stocks A and B,
        [x_A, x_B], that minimize the portfolio variance.

    """
    # Covariance matrix P
    covAB = rAB * np.sqrt(varA * varB)
    P = np.array([[varA, covAB],
                  [covAB, varB]])
    # Weight vector
    x = cvx.Variable(2)
    # Objective
    objective = cvx.Minimize(cvx.quad_form(x, P))
    # Constraint
    constraints = [sum(x) == 1]

    problem = cvx.Problem(objective, constraints)
    problem.solve()
    xA, xB = x.value
    return xA, xB


def optimize_portfolio(returns, index_weights, scale=.00001):
    """
    Create a function that takes the return series of a set of stocks, the index weights,
    and scaling factor. The function will minimize a combination of the portfolio variance
    and the distance of its weights from the index weights.
    The optimization will be constrained to be long only, and the weights should sum to one.

    Parameters
    ----------
    returns : numpy.ndarray
        2D array containing stock return series in each row.

    index_weights : numpy.ndarray
        1D numpy array containing weights of the index.

    scale : float
        The scaling factor applied to the distance between portfolio and index weights

    Returns
    -------
    x : np.ndarray
        A numpy ndarray containing the weights of the stocks in the optimized portfolio
    """
    # number of stocks m is number of rows of returns, and also number of index weights
    m = returns.shape[0]
    P = np.cov(returns)
    # Weights vector
    x = cvx.Variable(m)
    # Portfolio variance
    portfolio_var = cvx.quad_form(x, P)
    # Euclidean distance (L2 norm) between portfolio and index weights
    distance_to_index = cvx.norm(x - index_weights, p=2)
    # Objective function
    objective = cvx.Minimize(portfolio_var + scale * distance_to_index)
    # Constraints
    constraints = [sum(x) == 1, x >= 0]

    problem = cvx.Problem(objective, constraints)
    problem.solve()
    return x.value


if __name__ == '__main__':
    quiz_tests.test_optimize_twoasset_portfolio(optimize_twoasset_portfolio)
    quiz_tests.test_optimize_portfolio(optimize_portfolio)
