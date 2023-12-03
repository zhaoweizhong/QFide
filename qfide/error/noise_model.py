import numpy as np
from qiskit.quantum_info import Operator
from qiskit.providers.aer.noise import (
    NoiseModel,
    QuantumError,
    depolarizing_error,
    amplitude_damping_error,
    phase_damping_error,
    phase_amplitude_damping_error,
    coherent_unitary_error,
)


def depolarizing_noise(prob: float) -> NoiseModel:
    """
    Generate a depolarizing noise model.

    Parameters
    ----------
    prob : float
        The probability of the error.

    Returns
    -------
    NoiseModel
        The noise model.
    """
    error = depolarizing_error(prob, 2)
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(error, ["cx", "cz"])  # Appying to two-qubit gates
    return noise_model


def amplitude_damping_noise(prob: float) -> NoiseModel:
    """
    Generate an amplitude damping noise model.

    Parameters
    ----------
    prob : float
        The probability of the error.

    Returns
    -------
    NoiseModel
        The noise model.
    """
    error = amplitude_damping_error(prob)
    control = QuantumError(error.tensor(Operator(np.eye(2))))
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(control, ["cx", "cz"])  # Appying to two-qubit gates
    return noise_model


def phase_damping_noise(prob: float) -> NoiseModel:
    """
    Generate a phase damping noise model.

    Parameters
    ----------
    prob : float
        The probability of the error.

    Returns
    -------
    NoiseModel
        The noise model.
    """
    error = phase_damping_error(prob)
    control = QuantumError(error.tensor(Operator(np.eye(2))))
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(control, ["cx", "cz"])  # Appying to two-qubit gates
    return noise_model


def phase_amplitude_damping_noise(prob_pha: float, prob_amp: float) -> NoiseModel:
    """
    Generate a phase and amplitude damping noise model.

    Parameters
    ----------
    prob_pha : float
        The probability of the phase damping error.
    prob_amp : float
        The probability of the amplitude damping error.

    Returns
    -------
    NoiseModel
        The noise model.
    """
    error = phase_amplitude_damping_error(prob_amp, prob_pha)
    control = QuantumError(error.tensor(Operator(np.eye(2))))
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(control, ["cx", "cz"])  # Appying to two-qubit gates
    return noise_model


def coherent_unitary_noise() -> NoiseModel:
    """
    Generate a coherent unitary noise model.

    Returns
    -------
    NoiseModel
        The noise model.
    """
    unitary_matrix = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
    error = coherent_unitary_error(unitary_matrix)
    control = QuantumError(error.tensor(Operator(np.eye(2))))
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(control, ["cx", "cz"])  # Appying to two-qubit gates
    return noise_model
