from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ
from numpy import pi

circuit = QuantumCircuit(3, 3)    # init 3 qubit system

circuit.x(0)    # Not gate on qubit 0
circuit.x(2)    # Not gate on qubit 2

circuit.h(2)              # Hadamard gate on qubit 2
circuit.cp(pi/2, 2, 1)    # rotates q1 if q2 is in |1>
circuit.cp(pi/4, 2, 0)    # rotates q0 if q2 is in |1> 

circuit.h(1)   
circuit.cp(pi/2, 1, 0)    # rotates q0 if q1 is in |1> 

circuit.h(0)    
circuit.swap(0, 2)  # swaps qubit 0 & 2

IBMQ.save_account('''API TOKEN GOES HERE''')
IBMQ.load_account()

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibm_perth')
job = execute(circuit, backend=qcomp)
job_monitor(job)                            # add the job to the queue


result = job.result()                       # grab results form the job
plot_histogram(result.get_counts(circut))   # plots histogram of quatum state