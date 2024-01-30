import time
from utilities.data_loader import txtLoader
from utilities.statistics import statistics

start_time = time.time()

numbers = txtLoader()

measures = statistics(numbers)

end_time = time.time()

results = (f'Mean: {measures.mean()}\n'
           f'Median: {measures.median()}\n'
           f'Mode: {measures.mode()}\n'
           f'Standard deviation: {measures.standard_deviation()}\n'
           f'Variance: {measures.variance()}\n'
           f'Execution time: {end_time - start_time} seconds')

print(results)

with open('StatisticsResults.txt', 'w') as output:
    print(results, file=output)
