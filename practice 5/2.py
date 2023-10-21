from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size != 2:
    if rank == 0:
        print("This program has 2 processes.")
    exit(0)

for i in range(1, 101):
    if rank == 0:
        message = i
        comm.send(message, dest=1)
        received_message = comm.recv(source=1)
        print(f"Processor 0 sent {message} and received {received_message}")
    
    elif rank == 1:
        received_message = comm.recv(source=0)
        incremented_message = received_message + 1
        comm.send(incremented_message, dest=0)