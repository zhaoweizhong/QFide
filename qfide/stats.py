import numpy as np
from typing import List
from scipy import stats


def stats_calc(sim: List[float], exp=[0.707, 0.696, 0.698, 0.671]):
    """
    Calculate the statistics of the results.

    Parameters
    ----------
    sim : List[float]
        The list of simulation results.
    exp : List[float]
        The list of experimental results.

    Returns
    -------
    None
    """
    exp = np.array(exp)  # 00, 01, 10, 11
    sim = np.array(sim)

    # Mean Absolute Difference (MAD)
    mad = np.mean(np.abs(sim - exp))

    # T-test for paired samples
    t_statistic, p_value_t_test = stats.ttest_rel(sim, exp)

    # Wilcoxon signed-rank test
    wilcoxon_statistic, p_value_wilcoxon = stats.wilcoxon(sim, exp)

    print("Mean Absolute Difference (MAD):", mad)
    print("T-test:", t_statistic, "P-value:", p_value_t_test)
    print("Wilcoxon:", wilcoxon_statistic, "P-value:", p_value_wilcoxon)
