# Mean Deviation from Median - Discrete Frequency Distribution

x = list(map(float, input("Enter the values of x: ").split()))
f = list(map(int, input("Enter the frequencies: ").split()))

# Total frequency
N = sum(f)

# Find median
cumulative_frequency = 0
median = 0

for i in range(len(x)):
    cumulative_frequency += f[i]

    if cumulative_frequency >= (N + 1) / 2:
        median = x[i]
        break

# Calculate Mean Deviation from Median
total_deviation = 0

for i in range(len(x)):
    total_deviation += f[i] * abs(x[i] - median)

mean_deviation = total_deviation / N

print("Total Frequency:", N)
print("Median:", median)
print("Mean Deviation from Median:", mean_deviation)
