import numpy as np
import matplotlib.pyplot as plt

# Define the conditions for the domain
def domain_condition(x, y):
    return np.logical_and(y >= x, y + x > 0)

# Generate points within a specified range
x_values = np.linspace(-5, 5, 400)
y_values = np.linspace(-5, 5, 400)

# Create a meshgrid of (x, y) values
X, Y = np.meshgrid(x_values, y_values)

# Apply the domain condition to get a mask
domain_mask = domain_condition(X, Y)

# Apply the mask to keep only valid points
X_valid = np.ma.masked_where(~domain_mask, X)
Y_valid = np.ma.masked_where(~domain_mask, Y)

# Plot the valid points
plt.figure(figsize=(8, 6))
plt.pcolormesh(X, Y, domain_mask, shading='auto', cmap='viridis', alpha=0.1)
plt.scatter(X_valid, Y_valid, color='blue', s=2, label='Valid Points')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Domain of $f(x, y) = \sqrt{y-x} \ln(y+x)$')

# Add legend
plt.legend()

# Show the plot
plt.show()