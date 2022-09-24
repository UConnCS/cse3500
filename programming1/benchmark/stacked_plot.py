from matplotlib import pyplot as plt
import json

dp_data = []

with open("dp_runtimes.txt", "r") as f:
    # data is comma delimited pixels,time
    data = f.read().splitlines()
    data = [line.split(",") for line in data]
    data = [(int(pixels), int(float(time) * 1000)) for pixels, time in data]

    x, y = list(map(lambda x: x[0], data)), list(map(lambda x: x[1], data))
    # put tuples into dp_data
    dp_data = list(zip(x, y))

# same as above, but for greedy
greedy_data = []
with open("naive_runtimes.txt", "r") as f:
    # data is comma delimited pixels,time
    data = f.read().splitlines()
    data = [line.split(",") for line in data]
    data = [(int(pixels), int(float(time) * 1000)) for pixels, time in data]

    x, y = list(map(lambda x: x[0], data)), list(map(lambda x: x[1], data))
    # put tuples into greedy_data
    greedy_data = list(zip(x, y))

# plot dp in blue
plt.plot(*zip(*dp_data), color="blue", label="Dynamic Programming")

#plot greedy in red
plt.plot(*zip(*greedy_data), color="red", label="Naive")

plt.title("Pixel Count vs Time (Dynamic Programming vs Naive)")
# legend
plt.legend()

plt.xlabel("Pixel Count")
plt.ylabel("Time (ms)")
plt.savefig("stacked_runtimes.png")
