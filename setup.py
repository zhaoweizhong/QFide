from setuptools import setup, find_packages

setup(
    name="qfide",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["qiskit", "qiskit-aer", "numpy", "matplotlib", "scipy", "pylatexenc"],
)
