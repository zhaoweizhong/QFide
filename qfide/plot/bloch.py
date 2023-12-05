from qiskit import Aer, QuantumCircuit, execute
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt


def plot_bloch(circuit: QuantumCircuit, save_figure=False, save_dir="figures"):
    """
    Plot the bloch sphere of the circuit.

    Parameters
    ----------
    circuit : QuantumCircuit
        The circuit to be plotted.
    save_figure : bool
        Whether to save the figure.
    save_dir : str
        The directory to save the figure.

    Returns
    -------
    None
    """
    backend = Aer.get_backend("statevector_simulator")
    out_vector = execute(circuit, backend).result().get_statevector()
    plot_bloch_multivector(out_vector)
    if save_figure:
        plt.savefig(f"{save_dir}/bloch.svg", format="svg")
    else:
        plt.show()
    plt.close()
