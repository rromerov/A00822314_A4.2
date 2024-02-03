"""
Module to compute statistics on a set of numbers loaded from a text file.
"""
# Import libraries
import time
from prettytable import PrettyTable
from utilities.data_loader import stadistic_data
from utilities.statistics import Statistics

# Record the start time of the script execution
start_time = time.time()

# Load data for statistical analysis, separating numeric and non-numeric values
numbers, not_numbers = stadistic_data()

# Create an instance of the Statistics class with the numeric data
measures = Statistics(numbers)

# Record the end time of the script execution
end_time = time.time()

# Create a PrettyTable object to display the statistical results
results = PrettyTable()

# Set the column names for the table
results.field_names = ['Count', 'Valid', 'Mean', 'Median', 'Mode',
                       'Standard deviation', 'Variance']

# Add a row to the table with statistical measures
results.add_row([measures.valid_count() + len(not_numbers),
                 measures.valid_count(), measures.mean(),
                 measures.median(), measures.mode(),
                 measures.standard_deviation(),
                 measures.variance()])

# Calculate the execution time of the script
execution_time = f'Execution time: {time.time() - start_time:.12f} seconds'

# Combine the statistical results and execution time for printing
end_result = f'{results}\n{execution_time}'

# Print the statistical results and execution time
print(end_result)

# Write the statistical results and execution time to a text file
with open('StatisticsResults.txt', 'w', encoding='utf-8') as output:
    output.write(end_result)
