import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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

# Interpolate the x values for the given y values
y_values = [10, 30, 60]
interpolator = interp1d(y_data, x_data)
x_values = interpolator(y_values)

# Print the corresponding x values
for y, x in zip(y_values, x_values):
    print(f'x value for y = {y}: {x}')

plt.show()
