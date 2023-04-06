import statistics
import math

AO5 = 1

while AO5 == 1:
    times = [
    float(input("Time 1\n")),
    float(input("Time 2\n")),
    float(input("Time 3\n")),
    float(input("Time 4\n")),
    float(input("Time 5\n"))
    ]

    times.remove(max(times))

    times.remove(min(times))

    print(statistics.mean(times))

    AO5 = int(input("Input 1 to do another average of 5 again, 2 to stop"))
exit