import numpy as np
from typing import List
from scipy import stats


def stats_calc(sim: List[float], exp=[0.707, 0.696, 0.698, 0.671], save_file=False, save_dir="results"):
    """
    Calculate the statistics of the results.

    Parameters
    ----------
    sim : List[float]
        The list of simulation results.
    exp : List[float]
        The list of experimental results.
    save_file : bool
        Whether to save the results to a file.
    save_dir : str
        The directory to save the results.

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

    if save_file:
        with open(f"{save_dir}/stats.txt", "w") as f:
            f.write(f"Mean Absolute Difference (MAD): {mad}\n")
            f.write(f"T-test: {t_statistic}, P-value: {p_value_t_test}\n")
            f.write(f"Wilcoxon: {wilcoxon_statistic}, P-value: {p_value_wilcoxon}\n")
    else:
        print("Mean Absolute Difference (MAD):", mad)
        print("T-test:", t_statistic, "P-value:", p_value_t_test)
        print("Wilcoxon:", wilcoxon_statistic, "P-value:", p_value_wilcoxon)
