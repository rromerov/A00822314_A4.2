from utilities.dataLoader import txtLoader
from utilities.statistics import statistics

numbers = txtLoader()
measures = statistics(numbers)

print(f'Mean: {measures.mean()}')
print(f'Median: {measures.median()}')
print(f'Standard deviation: {measures.standard_deviation()}')
print(f'Variance: {measures.variance()}')

with open('StatisticsResults.txt', 'w') as output:
    print(f'Mean: {measures.mean()}', file = output)
    print(f'Median: {measures.median()}', file = output)
    print(f'Standard deviation: {measures.standard_deviation()}', file = output)
    print(f'Variance: {measures.variance()}', file = output)

