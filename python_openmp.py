import os
from time import time
import numpy as np

# Print the number of processors being used (default to 1 if not specified)
print("Using %d processors" % int(os.getenv("SLURM_CPUS_PER_TASK", 1)))

# Define the number of rounds for the loop
nrounds = 5

# Record the start time for performance measurement
t_start = time()

# Loop through the specified number of rounds
for i in range(nrounds):
    # Generate a random symmetric matrix of size 2000x2000
    a = np.random.random([2000, 2000])
    a = a + a.T  # Make the matrix symmetric by adding its transpose
    # Compute the (Moore-Penrose) pseudo-inverse of the matrix
    b = np.linalg.pinv(a)

# Calculate the total time taken for the specified number of rounds
t_delta = time() - t_start

# Print the time taken to invert the specified number of symmetric 2000x2000 matrices
print(
    "Seconds taken to invert %d symmetric 2000x2000 matrices: %f" % (nrounds, t_delta)
)
