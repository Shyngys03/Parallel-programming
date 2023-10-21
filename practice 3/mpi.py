from mpi4py import MPI

# function to be integrated
def f(x):
    return x**2

# integral limits
a = 0.0
b = 1.0
n = 1000000  # number of subintervals

def midpoint_rule(start, end, n):
    h = (end - start) / n
    sum = 0.0

    for i in range(start, end):
        x = start + (i + 0.5) * h
        sum += f(x)
    
    return h * sum


def trapezoidal_rule(start, end, n):
    h = (end - start) / n
    sum = 0.5 * (f(start) + f(end))

    for i in range(1, n):
        x = start + i * h
        sum += f(x)

    return h * sum


def simpsons_rule(start, end, n):
    h = (end - start) / n
    sum = f(start) + f(end)

    for i in range(1, n, 2):
        x = start + i * h
        sum += 4 * f(x)
    
    for i in range(2, n - 1, 2):
        x = start + i * h
        sum += 2 * f(x)
    
    return h * sum / 3


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Divide the subintervals among processes
    subintervals_per_process = n // size
    start = rank * subintervals_per_process
    end = start + subintervals_per_process

    # Compute the integral using the selected rule
    if rank == 0:
        start_time = MPI.Wtime()

    result = midpoint_rule(start, end, subintervals_per_process)
    #result = trapezoidal_rule(start, end, subintervals_per_process)
    #result = simpsons_rule(start, end, subintervals_per_process)
    
    total_result = comm.reduce(result, op=MPI.SUM, root=0)

    if rank == 0:
        end_time = MPI.Wtime()
        execution_time = end_time - start_time
        print("Result:", total_result)
        print("Execution Time:", execution_time)
