from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = 2
second_rank = 

for i in range(1, 100):
    print(f'Processor {rank} counts {i} and sends message to processor {second_rank}')