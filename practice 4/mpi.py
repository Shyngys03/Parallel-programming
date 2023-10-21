from mpi4py import MPI
import random

num_points = 1000000

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

points_inside_circle = 0

for _ in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x**2 + y**2 <= 1:
        points_inside_circle += 1

if rank != 0:
    comm.send(points_inside_circle, dest=0)
else:
    total_points_inside_circle = points_inside_circle
    for i in range(1, size):
        received_points = comm.recv(source=i)
        total_points_inside_circle += received_points

    pi_estimate = (4 * total_points_inside_circle) / (num_points * size)
    print("Estimated Pi:", pi_estimate)