import matplotlib.pyplot as plt
from typing import List


def plot_fidelity(x: List[float], y: List[float]):
    """
    Plot the fidelity of the results.

    Parameters
    ----------
    x : List[float]
        The list of results.
    y : List[float]
        The list of fidelity of the results.

    Returns
    -------
    None
    """
    plt.bar(x, y, width=0.5, fc="#648fff", zorder=2)
    plt.grid(ls="--", alpha=0.8, axis="y")
    plt.xlabel("BSM Results")
    plt.ylabel("Fidelity")
    for i in range(len(x)):
        plt.text(list(x)[i], list(y)[i], str(round(list(y)[i], 3)), ha="center", va="bottom")
    plt.show()
