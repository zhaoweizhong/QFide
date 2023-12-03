from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as plt


def plot_tomography(qc: QuantumCircuit):
    """
    Plot the tomography of the given circuit.

    Parameters
    ----------
    qc : QuantumCircuit
        The circuit to be plotted.

    Returns
    -------
    None
    """
    state = DensityMatrix(qc)
    plot_state_city(state)
    plt.show()
