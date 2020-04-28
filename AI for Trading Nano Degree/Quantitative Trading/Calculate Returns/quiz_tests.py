import sys

sys.path.append("../../")
from quiz import calculate_returns

from collections import OrderedDict
import numpy as np
import pandas as pd
from tests import project_test, generate_random_tickers, generate_random_dates, \
    assert_output


@project_test
def test_calculate_returns(fn=calculate_returns):
    tickers = generate_random_tickers(5)
    dates = generate_random_dates(6)

    fn_inputs = {
        'close': pd.DataFrame(
            [
                [21.050810483942833, 17.013843810658827, 10.984503755486879,
                 11.248093428369392, 12.961712733997235],
                [15.63570258751384, 14.69054309070934, 11.353027688995159,
                 475.74195118202061, 11.959640427803022],
                [482.34539247360806, 35.202580592515041, 3516.5416782257166,
                 66.405314327318209, 13.503960481087077],
                [10.918933017418304, 17.9086438675435, 24.801265417692324,
                 12.488954191854916, 10.52435923388642],
                [10.675971965144655, 12.749401436636365, 11.805257579935713,
                 21.539039489843024, 19.99766036804861],
                [11.545495378369814, 23.981468434099405, 24.974763062186504,
                 36.031962102997689, 14.304332320024963]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'returns',
            pd.DataFrame(
                [
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [-0.25723988, -0.13655355, 0.03354944, 41.29534136,
                     -0.07731018],
                    [29.84897463, 1.39627496, 308.74483411, -0.86041737,
                     0.12912763],
                    [-0.97736283, -0.49126900, -0.99294726, -0.81192839,
                     -0.22064647],
                    [-0.02225135, -0.28808672, -0.52400584, 0.72464717,
                     0.90013092],
                    [0.08144677, 0.88098779, 1.11556274, 0.67286764,
                     -0.28469971]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)
