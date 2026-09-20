# Mean Deviation from Median - Ungrouped Data

data = list(map(float, input("Enter the observations: ").split()))

# Sort the data
data.sort()

# Find median
n = len(data)

if n % 2 == 0:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
else:
    median = data[n // 2]

# Calculate mean deviation from median
deviations = [abs(x - median) for x in data]
mean_deviation = sum(deviations) / n

print("Sorted Data:", data)
print("Median:", median)
print("Mean Deviation from Median:", mean_deviation)
