
from mpi4py import MPI
import numpy as np

data = [5, 3, 8, 1, 7, 9, 4, 2]

comm = MPI.COMM_WORLD

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
    
chunk_size = len(data) // size
local_data = data[rank * chunk_size:(rank + 1) * chunk_size]

local_min = min(local_data)
local_max = max(local_data)

min_max_data = comm.gather((local_min, local_max), root=0)

if rank == 0:
    min_values, max_values = zip(*min_max_data)

    global_min = min(min_values)
    global_max = max(max_values)
        
    print("Global Minimum:", global_min)
    print("Global Maximum:", global_max)