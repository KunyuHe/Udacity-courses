import quiz_tests
from scipy import stats


def is_normal_ks(sample, test=stats.kstest, p_level=0.05, **kwargs):
    """
    sample: a sample distribution
    test: a function that tests for normality
    p_level: if the test returns a p-value > than p_level, assume normality

    return: True if distribution is normal, False otherwise
    """
    normal_args = (sample.mean(), sample.std())

    t_stat, p_value = test(sample, 'norm', normal_args, **kwargs)
    print("Test statistic: {}, p-value: {}".format(t_stat, p_value))
    print("Is the distribution Likely Normal? {}\n".format(p_value > p_level))

    return p_value > p_level


if __name__ == "__main__":
    quiz_tests.test_is_normal_ks(is_normal_ks)
