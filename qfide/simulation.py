from typing import List
from qiskit.providers.aer.noise import NoiseModel
from qiskit.quantum_info import Operator
from qfide.teleportation import teleport
from qfide.fidelity import fidelity_calc
from qfide.plot.fidelity import plot_fidelity
from qfide.plot.tomography import plot_tomography
from qfide.plot.bloch import plot_bloch


def run_sim(
    noise_model: NoiseModel,
    loss_model: Operator,
    runs=1000,
    draw_circuit_first=False,
    mpl_output=True,
    fidelity_plot=False,
    tomography_plot=False,
    bloch_plot=False,
    save_figure=False,
    save_dir="figures",
) -> List[float]:
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
    save_figure : bool
        Whether to save the figure.
    save_dir : str
        The directory to save the figure.

    Returns
    -------
    List[float]
        The list of fidelity of the results.
    """
    f_00 = []
    f_01 = []
    f_10 = []
    f_11 = []
    for run in range(runs):
        teleport_result = teleport(
            noise_model=noise_model,
            loss_model=loss_model,
            draw_circuit=(draw_circuit_first and run == 0),
            mpl_output=mpl_output,
            shots=1000,
            save_figure=save_figure,
            save_dir=save_dir,
        )
        counts = {k: v for k, v in sorted(teleport_result.items())}
        res = fidelity_calc(counts)
        if res[0] != 0:
            f_00.append(res[0])
        if res[1] != 0:
            f_01.append(res[1])
        if res[2] != 0:
            f_10.append(res[2])
        if res[3] != 0:
            f_11.append(res[3])

    x = ["00", "01", "10", "11"]
    y = [sum(f_00) / len(f_00), sum(f_01) / len(f_01), sum(f_10) / len(f_10), sum(f_11) / len(f_11)]
    y_max = [max(f_00), max(f_01), max(f_10), max(f_11)]
    y_min = [min(f_00), min(f_01), min(f_10), min(f_11)]

    if fidelity_plot:
        plot_fidelity(x, y, y_max, y_min, save_figure=save_figure, save_dir=save_dir)
    if tomography_plot:
        circuit = teleport(noise_model=noise_model, loss_model=loss_model, draw_circuit=False, shots=1000, no_measure=True, save_figure=False)
        plot_tomography(circuit, save_figure=save_figure, save_dir=save_dir)
    if bloch_plot:
        circuit = teleport(noise_model=noise_model, loss_model=loss_model, draw_circuit=False, shots=1000, no_measure=True, save_figure=False)
        plot_bloch(circuit, save_figure=save_figure, save_dir=save_dir)

    return y
