import matplotlib.pyplot as plt

# Data for frequency distribution
score_ranges = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70"]
midpoints = [5, 15, 25, 35, 45, 55, 65]  # Midpoints of each score range
frequencies = [2, 5, 8, 12, 7, 4, 2]

# Plotting the frequency polygon
plt.figure(figsize=(10, 6))
plt.plot(midpoints, frequencies, marker='o', linestyle='-', color='b')
plt.title('Frequency Polygon of Test Scores')
plt.xlabel('Score Range Midpoints')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
