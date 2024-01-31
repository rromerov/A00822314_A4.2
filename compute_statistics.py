"""
Module to compute statistics on a set of numbers loaded from a text file.
"""
import time
from utilities.data_loader import txt_loader
from utilities.statistics import Statistics

start_time = time.time()

numbers = txt_loader()

measures = Statistics(numbers)

end_time = time.time()

results = (f'Mean: {measures.mean()}\n'
           f'Median: {measures.median()}\n'
           f'Mode: {measures.mode()}\n'
           f'Standard deviation: {measures.standard_deviation()}\n'
           f'Variance: {measures.variance()}\n'
           f'Execution time: {end_time - start_time} seconds')

print(results)

with open('StatisticsResults.txt', 'w', encoding='utf-8') as output:
    print(results, file=output)
