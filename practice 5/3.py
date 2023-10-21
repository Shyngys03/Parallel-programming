from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 4

if n < 2:
    if rank == 0:
        print("This program has at least 2 processes.")
    exit(0)

if size < n:
    if rank == 0:
        print(f"This program requires at least {n} processes.")
    exit(0)

sender_rank = rank
receiver_rank = (rank + 1) % n

for i in range(n):
    if rank == sender_rank:
        message = f"Process {rank} sent to process {receiver_rank}"
        comm.send(message, dest=receiver_rank)
        print(message)

    elif rank == receiver_rank:
        received_message = comm.recv(source=sender_rank)
        print(received_message)
        
    sender_rank = (sender_rank + 1) % n
    receiver_rank = (receiver_rank + 1) % n