import numpy as np
import math
import random
from qiskit.quantum_info import Operator


def loss_model() -> Operator:
    """
    Generate a loss model.

    Returns
    -------
    Operator
        The loss model.
    """
    gamma = random.gauss(0.5, 0.1)
    msr = math.sqrt(1 - gamma)
    sr = math.sqrt(gamma)
    density_matrix = np.array([[1, 0, 0, 0], [0, msr, sr, 0], [0, -sr, msr, 0], [0, 0, 0, 1]])
    unitary_gate = Operator(density_matrix)
    return unitary_gate.to_instruction()
