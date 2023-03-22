import numpy as np
import matplotlib.pyplot as plt

def find_x_for_y(y_target, x_data, y_data):
    for i in range(len(y_data) - 1):
        if y_data[i] >= y_target > y_data[i+1]:
            x1, x2 = x_data[i], x_data[i+1]
            y1, y2 = y_data[i], y_data[i+1]
            x_target = x1 + (x2 - x1) * (y_target - y1) / (y2 - y1)
            return x_target
    return None

# Read data from the file
filename = 'dat_opal.txt'
data = np.loadtxt(filename)
x_data = data[:, 0]
y_data = data[:, 1]

# Create a scatter plot with a line connecting the dots on a semi-log graph
plt.figure()
plt.scatter(x_data, y_data, marker='o', color='blue')
plt.plot(x_data, y_data, linestyle='-', color='blue')
plt.xscale('log')
plt.xlabel('Sieve Opening (mm)')
plt.ylabel('Percent Finer by Weight')
plt.title('Semi-log graph of Sieve Opening vs Percent Finer by Weight')

# Find the corresponding x values for the given y values
y_values = [10, 30, 60]
x_values = [find_x_for_y(y, x_data, y_data) for y in y_values]

# Print the corresponding x values
for y, x in zip(y_values, x_values):
    print(f'x value for y = {y}: {x}')

plt.show()
