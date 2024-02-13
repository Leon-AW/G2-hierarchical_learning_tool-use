import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


# FC
logs1 = [
    0, 4, 0, 0, 1, 0, 2, 1, 1, 1, 0, 0, 3, 1, 1, 2, 0, 0, 0, 2,
    93, 77, 82, 67, 75, 67, 71, 63, 77, 62, 64, 85, 67, 66, 68, 78,
    72, 74, 69, 63, 4, 0, 3, 1, 0, 2, 1, 0, 1, 4, 1, 0, 2, 4,
    0, 1, 2, 0, 1, 2, 54, 54, 47, 50, 38, 63, 54, 55, 57, 66, 68,
    64, 67, 58, 51, 56, 56, 52, 75, 61, 2, 3, 2, 3, 2, 1, 1, 4,
    0, 1, 0, 2, 0, 2, 1, 2, 1, 3, 2
]

# SGS
logs2 = [
    5, 3, 0, 1, 3, 0, 2, 7, 0, 1, 1, 0, 4, 2, 1, 2, 0, 2, 1, 2,
    2, 0, 0, 3, 1, 2, 1, 3, 0, 2, 2, 1, 3, 3, 0, 3, 3, 2, 3, 1,
    2, 0, 1, 0, 0, 0, 0, 0, 0, 4, 2, 0, 2, 1, 1, 3, 0, 1, 5, 1,
    3, 1, 2, 0, 1, 4, 1, 0, 6, 1, 0, 1, 2, 0, 2, 1, 2, 0, 1, 2,
    2, 2, 3, 0, 1, 4, 2, 1, 0, 2, 0, 0, 0, 2, 0, 1, 0, 3, 2
]

# FRGB
logs3 = [
    0, 0, 0, 7, 24, 15, 26, 52, 55, 47, 44, 47, 69, 38, 51, 56, 53,
    56, 53, 69, 67, 73, 53, 64, 78, 72, 52, 73, 62, 63, 74, 67, 78,
    74, 65, 60, 67, 61, 71, 75, 61, 57, 66, 53, 65, 50, 83, 57, 68,
    66, 71, 61, 75, 68, 56, 77, 63, 64, 77, 63, 59, 72, 63, 61, 64,
    68, 65, 71, 59, 58, 75, 60, 65, 67, 78, 64, 69, 76, 66, 82, 69,
    56, 86, 63, 47, 62, 73, 75, 77, 56, 63, 72, 72, 89, 91, 76, 83,
    68, 65
]

# RMB
logs4 = [
    20, 32, 43, 27, 46, 29, 45, 24, 22, 32, 43, 37, 49, 36, 34, 37, 27,
    38, 36, 23, 36, 52, 33, 43, 26, 37, 30, 39, 32, 35, 22, 37, 38, 61,
    55, 49, 50, 57, 42, 54, 40, 57, 63, 57, 46, 51, 49, 59, 48, 49, 51,
    55, 44, 59, 59, 58, 49, 56, 82, 70, 74, 58, 62, 67, 84, 74, 73, 65,
    72, 70, 56, 77, 82, 68, 72, 58, 68, 83, 69, 63, 70, 71, 64, 77, 66,
    64, 89, 64, 75, 77, 83, 60, 80, 78, 77, 82, 79, 81, 70
]

# AMB
logs5 = [
    0, 0, 1, 0, 0, 1, 0, 0, 61, 195, 217, 210, 223, 216, 219, 203, 232, 220, 223, 219,
    216, 208, 224, 212, 209, 210, 224, 193, 213, 220, 205, 216, 210, 211, 212, 232, 212,
    207, 213, 202, 195, 211, 229, 220, 196, 216, 190, 197, 224, 235, 223, 221, 221, 224,
    219, 225, 223, 235, 223, 215, 219, 234, 230, 219, 217, 216, 235, 226, 209, 221, 215,
    212, 215, 228, 222, 214, 235, 241, 205, 218, 219, 202, 222, 223, 225, 206, 216, 226,
    213, 215, 217, 219, 219, 204, 220, 232, 216, 200, 199
]

# Calculate the total movements for each iteration
iterations = list(range(1000, 1000 + len(logs1) * 1000, 1000))
total_movements1 = logs1
total_movements2 = logs2
total_movements3 = logs3
total_movements4 = logs4
total_movements5 = logs5
print("length movement1", len(total_movements1))
print("length movement2", len(total_movements2))
print("length movement3", len(total_movements3))
print("length movement4", len(total_movements4))
print("length movement5", len(total_movements5))

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(iterations, total_movements1, marker='o', linestyle='-', label='25 none full True FC')
plt.plot(iterations, total_movements2, marker='o', linestyle='-', label='25 none full True SGS')
plt.plot(iterations, total_movements3, marker='o', linestyle='-', label='25 none full True FRGB')
plt.plot(iterations, total_movements4, marker='o', linestyle='-', label='25 none full True RMB')
plt.plot(iterations, total_movements5, marker='o', linestyle='-', label='25 none full True AMB')
plt.title('Total Movements vs Iteration')
plt.xlabel('Iteration')
plt.ylabel('Total Movements')
plt.legend()
plt.grid(True)

plt.show()