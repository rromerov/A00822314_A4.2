from utilities.dataLoader import txtLoader
from utilities.statistics import statistics

numbers = txtLoader()
measures = statistics(numbers)

print(f'Mean: {measures.mean()}\n'
      f'Median: {measures.median()}\n'
      f'Mode: {measures.mode()}\n'
      f'Standard deviation: {measures.standard_deviation()}\n'
      f'Variance: {measures.variance()}')


with open('StatisticsResults.txt', 'w') as output:
    print(f'Mean: {measures.mean()}\n'
          f'Median: {measures.median()}\n'
          f'Mode: {measures.mode()}\n'
          f'Standard deviation: {measures.standard_deviation()}\n'
          f'Variance: {measures.variance()}', file=output)


