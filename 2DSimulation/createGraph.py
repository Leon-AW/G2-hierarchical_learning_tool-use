import matplotlib.pyplot as plt

# Data from the logs
logs1 = [
    20, 32, 43, 27, 46, 29, 45, 24, 22, 32,
    43, 37, 49, 36, 34, 37, 27, 38, 36, 23,
    36, 52, 33, 43, 26, 37, 30, 39, 32, 35,
    22, 37, 38, 61, 55, 49, 50, 57, 42, 54,
    40, 57, 63, 57, 46, 51, 49, 59, 48, 49,
    51, 55, 44, 59, 59, 58, 49, 56, 82, 70,
    74, 58, 62, 67, 84, 74, 73, 65, 72, 70,
    56, 77, 82, 68, 72, 58, 68, 83, 69, 63,
    70, 71, 64, 77, 66, 64, 89, 64, 75, 77,
    83, 60, 80, 78, 77, 82, 79, 81, 70
]

logs2 = [
    1, 3, 4, 8, 8, 14, 7, 19, 7, 8,
    14, 13, 8, 5, 8, 5, 5, 9, 9, 5,
    8, 5, 9, 9, 8, 4, 13, 5, 5, 12,
    10, 9, 6, 11, 6, 10, 13, 15, 8, 4,
    10, 10, 6, 11, 10, 12, 9, 17, 9, 6,
    15, 10, 15, 9, 11, 14, 5, 10, 17, 13,
    6, 14, 6, 9, 5, 9, 8, 11, 6, 11,
    9, 11, 7, 11, 7, 8, 14, 9, 12, 12,
    8, 8, 5, 15, 6, 8, 12, 12, 9, 11,
    12, 14, 13, 13, 11, 16, 14, 15, 10
]

logs3 = [
    0, 6, 5, 6, 5, 9, 6, 7, 1, 2,
    8, 9, 10, 5, 13, 11, 5, 7, 8, 14,
    15, 8, 7, 5, 15, 9, 12, 14, 15, 12,
    14, 11, 10, 13, 16, 6, 15, 16, 7, 7,
    9, 22, 17, 15, 16, 19, 19, 25, 11, 10,
    16, 14, 13, 18, 17, 10, 16, 13, 16, 8,
    14, 21, 7, 17, 12, 13, 10, 19, 19, 16,
    8, 11, 11, 22, 22, 19, 27, 31, 18, 12,
    24, 13, 9, 13, 18, 13, 11, 14, 13, 14,
    8, 18, 15, 12, 23, 14, 12, 9, 27
]

logs4 = [
    5, 17, 27, 22, 17, 32, 28, 34, 30, 24,
    32, 31, 26, 29, 28, 15, 34, 25, 26, 23,
    28, 32, 29, 31, 24, 20, 38, 21, 21, 29,
    32, 36, 25, 32, 37, 21, 24, 29, 32, 31,
    21, 25, 27, 30, 28, 41, 41, 49, 49, 48,
    38, 45, 60, 44, 36, 41, 57, 47, 61, 51,
    46, 43, 40, 49, 52, 47, 40, 47, 44, 72,
    38, 50, 52, 51, 45, 41, 52, 51, 57, 40,
    61, 47, 51, 46, 49, 66, 40, 41, 55, 54,
    36, 40, 54, 36, 48, 55, 39, 53, 57
]

# Calculate the total movements for each iteration
iterations = list(range(1000, 1000 + len(logs1) * 1000, 1000))
total_movements1 = logs1
total_movements2 = logs2
total_movements3 = logs3
total_movements4 = logs4

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(iterations, total_movements1, marker='o', linestyle='-', label='25 none full True RMB')
plt.plot(iterations, total_movements2, marker='o', linestyle='-', label='25 both full True RMB')
plt.plot(iterations, total_movements3, marker='o', linestyle='-', label='50 both full True RMB')
plt.plot(iterations, total_movements4, marker='o', linestyle='-', label='50 none full True RMB')
plt.title('Total Movements vs Iteration')
plt.xlabel('Iteration')
plt.ylabel('Total Movements')
plt.legend()
plt.grid(True)
plt.show()

# Set custom x-axis tick labels
plt.xticks(iterations, [str(x * 10) for x in range(101)])

plt.grid(True)
plt.show()