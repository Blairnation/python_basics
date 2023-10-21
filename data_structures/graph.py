import matplotlib.pyplot as plt
import numpy as np

# Create an array of values for n
n = np.arange(1, 20)

# Define the functions
fa = 30 * n + 8
fb = n**2 + 1

# Plot the graphs
plt.figure(figsize=(10, 5))
plt.plot(n, fa, label='fa(n) = 30n + 8', color='blue')
plt.plot(n, fb, label='fb(n) = n^2 + 1', color='red')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('Function Value')
plt.legend()

# Find the intersection point
intersection_n = np.argwhere(fa > fb)[0][0]  # Find the first index where fa > fb
intersection_value = fa[intersection_n]

# Mark the intersection point
plt.plot(intersection_n, intersection_value, 'ro')  # 'ro' for red circle

# Annotate the intersection point
plt.annotate(f'Intersection\n({intersection_n}, {intersection_value})',
             xy=(intersection_n, intersection_value),
             xytext=(5, 100), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', color='black'))

# Show the plot
plt.grid(True)
plt.title('Comparison of fa(n) and fb(n)')
plt.show()
