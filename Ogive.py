import matplotlib.pyplot as plt

# Data for frequency distribution and cumulative frequency
score_ranges = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70"]
upper_class_boundaries = [10, 20, 30, 40, 50, 60, 70]  # Upper boundaries of each score range
frequencies = [2, 5, 8, 12, 7, 4, 2]

# Calculate cumulative frequencies
cumulative_frequencies = []
cumulative_sum = 0
for frequency in frequencies:
    cumulative_sum += frequency
    cumulative_frequencies.append(cumulative_sum)

# Plotting the ogive
plt.figure(figsize=(10, 6))
plt.plot(upper_class_boundaries, cumulative_frequencies, marker='o', linestyle='-', color='b')
plt.title('Ogive of Test Scores')
plt.xlabel('Score Range Upper Boundaries')
plt.ylabel('Cumulative Frequency')
plt.grid(True)
plt.show()
