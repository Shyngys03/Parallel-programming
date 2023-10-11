from math import sqrt
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

start1 = time.time()
const  = 2 * sqrt(3)
summ = 0

for i in range(100):
    summ += (-1)**i / (3**i * (2*i + 1))

pi1 = const * summ
end1 = time.time()

pi2 = 0
for i in range(100):
    pi2 += ((-0.25)**i) * ((2 / (4*i + 1)) + (2 / (4*i + 2)) + (1 / (4*i + 3))) 

end2 = time.time()

print(pi1, end1 - start1)
print(pi2, end2 - end1)

print(pi1 / pi2)