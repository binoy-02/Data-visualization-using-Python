import matplotlib.pyplot as plt

# Data
x1 = [3, 4, 7, 6, 5]
x2 = [2, 5, 9, 6, 8]
wins = [23, 12, 50, 70, 12]

# Plotting the bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(x1, x2, s=wins, alpha=0.5, c=wins, cmap='viridis')
plt.title('Bubble Chart of Wins')
plt.xlabel('x1')
plt.ylabel('x2')
plt.colorbar(label='Wins')
plt.grid(True)
plt.show()
