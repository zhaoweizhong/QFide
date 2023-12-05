import matplotlib.pyplot as plt
from typing import List
import numpy as np


def plot_fidelity(x: List[float], y: List[float], y_max: List[float], y_min: List[float], save_figure=False, save_dir="figures"):
    """
    Plot the fidelity of the results.

    Parameters
    ----------
    x : List[float]
        The list of results.
    y : List[float]
        The list of average fidelity of the results.
    y_max : List[float]
        The list of maximum fidelity of the results.
    y_min : List[float]
        The list of minimum fidelity of the results.
    save_figure : bool
        Whether to save the figure.
    save_dir : str
        The directory to save the figure.

    Returns
    -------
    None
    """
    yerr = [np.subtract(y, y_min), np.subtract(y_max, y)]
    plt.bar(x, y, yerr=yerr, width=0.5, fc="#648fff", zorder=2, capsize=5)
    plt.grid(ls="--", alpha=0.8, axis="y")
    plt.xlabel("BSM Results")
    plt.ylabel("Fidelity")
    for i in range(len(x)):
        plt.text(list(x)[i], list(y)[i], str(round(list(y)[i], 3)), ha="center", va="bottom")
    if save_figure:
        plt.savefig(f"{save_dir}/fidelity.svg", format="svg")
    else:
        plt.show()
    plt.close()
