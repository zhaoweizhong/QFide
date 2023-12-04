from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as plt


def plot_tomography(qc: QuantumCircuit, save_figure=False, save_dir="figures"):
    """
    Plot the tomography of the given circuit.

    Parameters
    ----------
    qc : QuantumCircuit
        The circuit to be plotted.
    save_figure : bool
        Whether to save the figure.
    save_dir : str
        The directory to save the figure.

    Returns
    -------
    None
    """
    state = DensityMatrix(qc)
    plot_state_city(state)
    if save_figure:
        plt.savefig(f"{save_dir}/tomography.svg", format="svg")
    else:
        plt.show()
    plt.close()
