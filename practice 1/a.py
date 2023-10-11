from mpi4py import MPI

s = "Hello World"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(s, rank)