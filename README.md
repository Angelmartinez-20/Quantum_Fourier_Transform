# Quantum Fourier Transform

Welcome to my analysis of the Quantum Fourier Transform (QFT)!

In this repository, you can find a research paper describing what the Quantum algorithm is and how it works. Additionally, there is Python code (QFT.py and IQFT.py) designed to work with the IBM Quantum Lab, and assembly code (QFT.asm and IQFT.asm) tailored for use with the IBM Quantum Composer.

## QFT
A 3-Qubit Quantum Fourier Transform Circuit designed for use on an IBM Quantum Computer. The input is a Quantum State of |101>, represented by a NOT gate on qubits 0 and 2. The output represents the quantum state frequency of its input, symbolized by the phase of each qubit. If you are familiar with the Fast Fourier Transform, the phase rotation gates essentially follow Euler's Formula. The Hadamard gates entangle the qubits as the algorithm runs in linear time, applying phase gates until all the qubits are covered. This is analogous to the concurrent process of the FFT. 

## IQFT
A 3-Qubit Inverse Quantum Fourier Transform Circuit designed for use on an IBM Quantum Computer. The input is frequencies of |101>, represented by a NOT gate on qubits 0 and 2, and Phase gates. The output represents the quantum state. This implementation is similar to the Inverse Fast Fourier Transform but in linear time.
