from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print(size, rank)


# a = list(map(int, input().split()))
# local_a = 


# maxi = -1000
# mini = 1000

# for i in range(len(a)):
#     print(rank)
#     if maxi < a[i]:
#         maxi = a[i]
#         print()
#     elif mini > a[i]:
#         mini = a[i]

# print(maxi, mini)