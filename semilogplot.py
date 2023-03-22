import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('dat_opal.txt')
x_data = data[:, 0]
y_data = data[:, 1]

# Plot data on semi-log graph
plt.scatter(x_data, y_data, color='blue', marker='o')
plt.plot(x_data, y_data, color='blue', linestyle='-', linewidth=1)
plt.xscale('log')
plt.xlabel('Sieve opening (mm)')
plt.ylabel('Percent finer by weight')
plt.title('Semi-log plot of Sieve Opening vs Percent finer by weight')

# Find the corresponding x values for y = 10, 30 and 60
y_values = [10, 30, 60]
x_corresponding = []

for y in y_values:
    idx = np.argmin(np.abs(y_data - y))
    x_corresponding.append(x_data[idx])

    # Plot the intersection point on the graph
    plt.scatter(x_data[idx], y, color='red', marker='x')
    plt.axhline(y, linestyle=':', color='gray', linewidth=1)
    plt.axvline(x_data[idx], linestyle=':', color='gray', linewidth=1)

# Print the corresponding x values
print("Corresponding x values for y = 10, 30 and 60:")
for i, y in enumerate(y_values):
    print(f"x({y}) = {x_corresponding[i]}")

plt.show()
