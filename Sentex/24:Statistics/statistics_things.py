import statistics

example_list = [2,5,5,6,6,9,90]

# Some statistical computations
mean = statistics.mean(example_list)
median = statistics.median(example_list)
standard_deviation = statistics.stdev(example_list)
variance = statistics.variance(example_list)

print(mean, median, standard_deviation, variance)
