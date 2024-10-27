from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def insertNumbers(n=1):
    ns = []
    check = False
    for i in range(n):
        while not check:
            try:
                inp = input(f'Insert the {i + 1} number:\n')
                ns.append(int(inp))
                check = True
            except:
                print('Error: Not a number. Reinsert\n')
        check = False
    return ns


def intstoBinary(ns):
    bs = []
    for nu in ns:
        bs.append(f'{nu:b}')
    return bs


def initializeCircuit(q_name, c_name, q_bits, c_bits):
    qregs = []
    cregs = []
    for i, qn in enumerate(q_name):
        qregs.append(QuantumRegister(q_bits[i], qn))
    for i, cn in enumerate(c_name):
        cregs.append(ClassicalRegister(c_bits[i], cn))
    circuit = QuantumCircuit(*qregs, *cregs)
    return qregs, cregs, circuit


def setRegAsBinary(qregs, binary, circuit):
    for i, qreg in enumerate(qregs):
        for j in range(len(binary[i]) - 1, -1, -1):
            if binary[i][j] == '1':
                circuit.x(qreg[len(binary[i]) - 1 - j])


def sum(qreg_q, qreg_q0, qreg_carry, creg, circuit):
    n, m = qreg_q.size, creg.size
    for i in range(n):
        #Save the carry
        circuit.ccx(qreg_q[i], qreg_q0[i], qreg_carry[i])
        #Sum q0[i] + q[i]
        circuit.cx(qreg_q[i], qreg_q0[i])
        #Sum the carry (q0[i]+ carry)
        if i > 0:
            circuit.ccx(qreg_carry[i-1], qreg_q0[i], qreg_carry[i])
            circuit.cx(qreg_carry[i-1], qreg_q0[i])

    for i in range(m - 1):
        circuit.measure(qreg_q0[i], creg[i])
    #Save the last carry in the +1 digit
    circuit.measure(qreg_carry[n - 1], creg[m - 1])
