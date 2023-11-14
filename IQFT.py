from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ
from numpy import pi

circuit = QuantumCircuit(3, 3)    # init 3 qubit system

# applies Hadamard to all 3 qubits
circuit.h(0)
circuit.h(1)
circuit.h(2)

# apply phase rotaiton gates to all 3 qubits
circuit.p(5 * pi / 4, 0)
circuit.p(5 * pi / 2, 1)
circuit.p(5 * pi, 2)

circuit.swap(0, 2)  # Swap qubits 0 and 2

circuit.h(0)

circuit.cp(-pi / 2, 0, 1) # rotates q2 if q1 is in |1>
circuit.h(1)

circuit.cp(-pi / 2, 1, 2) # rotates q2 if q1 is in |1>
circuit.cp(-pi / 4, 0, 2) # rotates q2 if q0 is in |1>
circuit.h(2)

IBMQ.save_account('''API TOKEN GOES HERE''')
IBMQ.load_account()

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibm_perth')
job = execute(circuit, backend = qcomp)  
job_monitor(job)                            # add the job to the queue


result = job.result()                       # grab results form the job
plot_histogram(result.get_counts(circut))   # plots histogram of quatum state