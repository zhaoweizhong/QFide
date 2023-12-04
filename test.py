import time
import os
from qfide.simulation import run_sim
from qfide.stats import stats_calc
from qfide.error.noise_model import depolarizing_noise, amplitude_damping_noise, phase_damping_noise, phase_amplitude_damping_noise, coherent_unitary_noise
from qfide.error.loss_model import loss_model


def run(noise_model, loss_model, runs, save_dir):
    directory = os.path.join(os.getcwd(), save_dir)
    os.makedirs(directory, exist_ok=True)
    start_time = time.time()
    with open(f"{save_dir}/time.txt", "w") as f:
        f.write(f"Start time: {time.ctime(start_time)}\n")
    counts = run_sim(
        noise_model=noise_model,
        loss_model=loss_model,
        runs=runs,
        draw_circuit_first=True,
        mpl_output=True,
        fidelity_plot=True,
        tomography_plot=True,
        save_figure=True,
        save_dir=save_dir,
    )
    stats_calc(counts, save_file=True, save_dir=save_dir)
    end_time = time.time()
    # print(f"Execution time: {end_time - start_time} seconds")
    with open(f"{save_dir}/time.txt", "a") as f:
        f.write(f"End time: {time.ctime(end_time)}\n")
        f.write(f"Execution time: {end_time - start_time} seconds\n")


run(noise_model=None, loss_model=None, runs=100000, save_dir="results/noise_none-loss_none-runs_100000")
run(noise_model=None, loss_model=loss_model(), runs=100000, save_dir="results/noise_none-loss_true-runs_100000")
run(noise_model=depolarizing_noise(0.15), loss_model=None, runs=100000, save_dir="results/noise_depolarizing-loss_none-runs_100000")
run(noise_model=depolarizing_noise(0.15), loss_model=loss_model(), runs=100000, save_dir="results/noise_depolarizing-loss_true-runs_100000")
run(noise_model=amplitude_damping_noise(0.2), loss_model=None, runs=100000, save_dir="results/noise_amplitude_damping-loss_none-runs_100000")
run(noise_model=amplitude_damping_noise(0.2), loss_model=loss_model(), runs=100000, save_dir="results/noise_amplitude_damping-loss_true-runs_100000")
run(noise_model=phase_damping_noise(0.2), loss_model=None, runs=100000, save_dir="results/noise_phase_damping-loss_none-runs_100000")
run(noise_model=phase_damping_noise(0.2), loss_model=loss_model(), runs=100000, save_dir="results/noise_phase_damping-loss_true-runs_100000")
run(noise_model=phase_amplitude_damping_noise(0.2, 0.2), loss_model=None, runs=100000, save_dir="results/noise_phase_amplitude_damping-loss_none-runs_100000")
run(noise_model=phase_amplitude_damping_noise(0.2, 0.2), loss_model=loss_model(), runs=100000, save_dir="results/noise_phase_amplitude_damping-loss_true-runs_100000")
run(noise_model=coherent_unitary_noise(), loss_model=None, runs=100000, save_dir="results/noise_coherent_unitary-loss_none-runs_100000")
run(noise_model=coherent_unitary_noise(), loss_model=loss_model(), runs=100000, save_dir="results/noise_coherent_unitary-loss_true-runs_100000")
