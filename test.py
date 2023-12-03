from qfide.simulation import run_sim
from qfide.stats import stats_calc

counts = run_sim(noise_model=False, loss_model=False, runs=1000, draw_circuit_first=True, mpl_output=True, fidelity_plot=True, tomography_plot=True)
stats_calc(counts)
