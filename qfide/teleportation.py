from qiskit import Aer, QuantumCircuit, execute
from qiskit.providers.aer.noise import NoiseModel
from qiskit.quantum_info import Operator
import matplotlib.pyplot as plt


def teleport(
    noise_model: NoiseModel, loss_model: Operator, draw_circuit=False, mpl_output=True, shots=1000, no_measure=False, save_figure=False, save_dir="figures"
) -> QuantumCircuit or (dict[str, int] or list[dict[str, int]]):
    """
    Run the teleportation circuit and return the result.

    Parameters
    ----------
    noise_model : NoiseModel
        The noise model to be used in the simulation.
    loss_model : Operator
        The loss model to be used in the simulation.
    draw_circuit : bool
        Whether to draw the circuit before the simulation.
    mpl_output : bool
        Whether to use matplotlib to draw the circuit. If false, the circuit will be printed in the console as text.
    shots : int
        The number of shots to be simulated.
    no_measure : bool
        Whether to return the circuit without measurement.
    save_figure : bool
        Whether to save the figure.
    save_dir : str
        The directory to save the figure.

    Returns
    -------
    QuantumCircuit or (dict[str, int] or list[dict[str, int]])
        The circuit if no_measure is True, otherwise the result.
    """
    circuit = QuantumCircuit(3, 3)

    # C prepares a Bell-pair
    circuit.h(1)
    circuit.cx(1, 2)
    circuit.barrier()  # Just a visual divider on graph

    # A entangles q0 and q1, and perform BSM
    circuit.cx(0, 1)
    circuit.h(0)

    # Loss Gate
    if loss_model:
        circuit.append(loss_model(), [0, 1])

    if not no_measure:
        circuit.measure([0, 1], [0, 1])
    circuit.barrier()  # Just a visual divider on graph

    # B uses BSM results to restore the state on q2
    circuit.cz(0, 2)
    circuit.cx(1, 2)
    circuit.barrier()  # Just a visual divider on graph

    # Loss Gate
    if loss_model:
        circuit.append(loss_model(), [0, 2])

    # Result Measurement
    if not no_measure:
        circuit.measure([2], [2])

    # Use simulator
    backend = Aer.get_backend("qasm_simulator")

    if draw_circuit:
        if mpl_output:
            circuit.draw(reverse_bits=True, output="mpl", style="clifford")
            if save_figure:
                plt.savefig(f"{save_dir}/circuit.svg", format="svg")
            else:
                plt.show()
            plt.close()
        else:
            print(circuit.draw(reverse_bits=True))

    # Run the circuit and get the result
    if noise_model:
        result = execute(circuit, backend, shots=shots, noise_model=noise_model).result()
    else:
        result = execute(circuit, backend, shots=shots).result()

    if no_measure:
        return circuit
    else:
        return result.get_counts(circuit)
