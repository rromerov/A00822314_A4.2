"""
Module to compute statistics on a set of numbers loaded from a text file.
"""
import time
from prettytable import PrettyTable
from utilities.data_loader import stadistic_data
from utilities.statistics import Statistics

start_time = time.time()

numbers, not_numbers = stadistic_data()

measures = Statistics(numbers)

end_time = time.time()

results = PrettyTable()

results.field_names = ['Count', 'Valid', 'Mean', 'Median', 'Mode',
                       'Standard deviation', 'Variance']

results.add_row([measures.valid_count() + len(not_numbers),
                 measures.valid_count(), measures.mean(),
                 measures.median(), measures.mode(),
                 measures.standard_deviation(),
                 measures.variance()])

execution_time = f'Execution time: {time.time() - start_time:.12f} seconds'

end_result = f'{results}\n{execution_time}'

print(end_result)

with open('StatisticsResults.txt', 'w', encoding='utf-8') as output:
    output.write(end_result)
