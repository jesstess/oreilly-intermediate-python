from matplotlib import pyplot

data = open("world_population.txt", "r").readlines()
dates = []
populations = []
for point in data:
    date, population = point.split()
    dates.append(date)
    populations.append(population)

pyplot.plot(dates, populations, "o-")
pyplot.ylabel("World population in millions")
pyplot.xlabel("Year")
pyplot.title("World population over time")
pyplot.show()
