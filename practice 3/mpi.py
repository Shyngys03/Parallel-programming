from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

func = 3 * x**2 + 1

