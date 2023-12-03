from typing import List
from qiskit.providers.aer.noise import NoiseModel
from qiskit.quantum_info import Operator
from qfide.teleportation import teleport
from qfide.fidelity import fidelity_calc
from qfide.plot.fidelity import plot_fidelity
from qfide.plot.tomography import plot_tomography


def run_sim(noise_model: NoiseModel, loss_model: Operator, runs=1000, draw_circuit_first=False, mpl_output=True, fidelity_plot=False, tomography_plot=False) -> List[float]:
    """
    Run the simulation and return the fidelity of the results.

    Parameters
    ----------
    noise_model : NoiseModel
        The noise model to be used in the simulation.
    loss_model : Operator
        The loss model to be used in the simulation.
    runs : int
        The number of runs to be simulated.
    draw_circuit_first : bool
        Whether to draw the circuit before the simulation.
    mpl_output : bool
        Whether to use matplotlib to draw the circuit. If false, the circuit will be printed in the console as text.
    fidelity_plot : bool
        Whether to plot the fidelity.
    tomography_plot : bool
        Whether to plot the tomography.

    Returns
    -------
    List[float]
        The list of fidelity of the results.
    """
    f_00 = 0
    count_00 = 0
    f_01 = 0
    count_01 = 0
    f_10 = 0
    count_10 = 0
    f_11 = 0
    count_11 = 0
    for run in range(runs):
        teleport_result = teleport(noise_model=noise_model, loss_model=loss_model, draw_circuit=(draw_circuit_first and run == 0), mpl_output=mpl_output, shots=1000)
        counts = {k: v for k, v in sorted(teleport_result.items())}
        res = fidelity_calc(counts)
        if res[0] != 0:
            f_00 += res[0]
            count_00 += 1
        if res[1] != 0:
            f_01 += res[1]
            count_01 += 1
        if res[2] != 0:
            f_10 += res[2]
            count_10 += 1
        if res[3] != 0:
            f_11 += res[3]
            count_11 += 1

    f_00 = f_00 / count_00
    f_01 = f_01 / count_01
    f_10 = f_10 / count_10
    f_11 = f_11 / count_11

    x = ["00", "01", "10", "11"]
    y = [f_00, f_01, f_10, f_11]

    if fidelity_plot:
        plot_fidelity(x, y)
    if tomography_plot:
        circuit = teleport(noise_model=noise_model, loss_model=loss_model, draw_circuit=False, shots=1000, no_measure=True)
        plot_tomography(circuit)

    return y
