from matplotlib import pyplot as plt
import json

with open("dp_runtimes.txt", "r") as f:
    # data is comma delimited pixels,time
    data = f.read().splitlines()
    data = [line.split(",") for line in data]
    data = [(int(pixels), int(float(time) * 1000)) for pixels, time in data]

    x, y = list(map(lambda x: x[0], data)), list(map(lambda x: x[1], data))
    print(x, y)

    plt.plot(x, y)

    plt.title("Pixel Count vs Time (Dynamic Programming)")
    plt.xlabel("Pixel Count")
    plt.ylabel("Time (ms)")
    plt.savefig("dp_runtimes.png")

