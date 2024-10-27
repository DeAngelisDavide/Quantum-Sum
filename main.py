from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import Session, SamplerV2 as Sampler

from utility import insertNumbers, intstoBinary, initializeCircuit, setRegAsBinary, sum

if __name__ == '__main__':
    numbers = insertNumbers(2)
    binary = intstoBinary(numbers)
    nbits = max(len(bi) for bi in binary)

    #Let's initialize the circuit *NOTE: For the sum all three registers must have the same number of bits
    qregs, cregs, circuit = initializeCircuit(['q', 'q0', 'carry'], ['c'], [nbits] * 3, [nbits + 1])
    setRegAsBinary(qregs[:2], binary, circuit)
    #Let's perform the sum
    sum(qregs[0], qregs[1], qregs[2], cregs[0], circuit)

    #Let's simulate the circuit
    aer_sim = AerSimulator()
    pm = generate_preset_pass_manager(backend=aer_sim, optimization_level=1)
    run_qc = pm.run(circuit)
    with Session(backend=aer_sim) as session:
        sampler = Sampler(mode=session)
        result = sampler.run([run_qc]).result()
        pub_result = result[0]

    #Check the result
    counts = pub_result.data.c.get_counts()
    print(f"Counts : {counts}")
    for binary, count in counts.items():
        print(f'Decimal Result: {int(binary, 2)}, Probability %{int(count / 1024) * 100}')

    circuit.draw("mpl").savefig('circuit.png')
