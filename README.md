# Quantum Adder
This project implements a generalized quantum adder that sums two non-negative integers using quantum circuits in Qiskit. 

## Overview

The quantum adder uses quantum gates to perform the addition operation. It is designed for educational purposes to demonstrate the principles of quantum computing and how quantum circuits can be constructed for basic arithmetic operations. In real applications Quantum algorithms that leverage superposition and other quantum properties are typically used for more efficient computations.

## How It Works

The code performs the following steps:
1. **Input**: The user is prompted to input two non-negative integers.
2. **Binary Conversion**: The integers are converted to their binary representation.
3. **Quantum Circuit Initialization**: Quantum and classical registers are created to hold the bits for the input numbers and the result.
4. **Sum Logic**: The quantum circuit implements the logic for adding two binary numbers.
5. **Simulation**: The quantum circuit is simulated using Qiskit Aer, and the results are outputted in decimal format.

## Usage

1. **Install Qiskit**: Ensure you have Qiskit, Qiskit-Aer and Qiskit-IBM-Runtime installed in your Python environment. You can install it via pip:

   ```
   pip install qiskit qiskit-aer qiskit-ibm-runtime

