from typing import List


def fidelity_calc(counts: dict[str, int] or list[dict[str, int]]) -> List[float]:
    """
    Calculate the fidelity of the results.

    Parameters
    ----------
    counts : dict[str, int] or list[dict[str, int]]
        The counts of the results.

    Returns
    -------
    List[float]
        The list of fidelity of the results.
    """
    start_qubit = 0
    # Name in q0, q1 format
    counts_bsm_00 = {bitstring: count for bitstring, count in counts.items() if bitstring[1:] == "00"}  # q1, q0 = 00
    counts_bsm_01 = {bitstring: count for bitstring, count in counts.items() if bitstring[1:] == "10"}  # q1, q0 = 10
    counts_bsm_10 = {bitstring: count for bitstring, count in counts.items() if bitstring[1:] == "01"}  # q1, q0 = 01
    counts_bsm_11 = {bitstring: count for bitstring, count in counts.items() if bitstring[1:] == "11"}  # q1, q0 = 11
    fidelity_00, fidelity_01, fidelity_10, fidelity_11 = 0, 0, 0, 0
    if counts_bsm_00 != 0:
        fidelity_00 = sum(count for bitstring, count in counts_bsm_00.items() if bitstring[0] == str(start_qubit)) / sum(count for bitstring, count in counts_bsm_00.items())
    if counts_bsm_01 != 0:
        fidelity_01 = sum(count for bitstring, count in counts_bsm_01.items() if bitstring[0] == str(start_qubit)) / sum(count for bitstring, count in counts_bsm_01.items())
    if counts_bsm_10 != 0:
        fidelity_10 = sum(count for bitstring, count in counts_bsm_10.items() if bitstring[0] == str(start_qubit)) / sum(count for bitstring, count in counts_bsm_10.items())
    if counts_bsm_11 != 0:
        fidelity_11 = sum(count for bitstring, count in counts_bsm_11.items() if bitstring[0] == str(start_qubit)) / sum(count for bitstring, count in counts_bsm_11.items())
    return [fidelity_00, fidelity_01, fidelity_10, fidelity_11]
