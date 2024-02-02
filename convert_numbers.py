"""
Module to convert decimal numbers to binary and hexadecimal from a text file.
"""
import time
from prettytable import PrettyTable
from utilities.data_loader import converter_data
from utilities.converter import Converter

# Record the start time of the script execution
start_time = time.time()

# Load decimal numbers using the converter_data function
decimals = converter_data()

# Create an instance of the Converter class with the loaded decimal numbers
conversions = Converter(decimals)

# Perform decimal-to-binary conversion
binaries = conversions.decimal_to_binary()

# Perform decimal-to-hexadecimal conversion
hexadecimals = conversions.decimal_to_hexadecimal()

# Create a table to display the results with appropriate column names
results = PrettyTable()

# Set the column names for the table
results.field_names = ['Number', 'Decimal', 'Binary', 'Hexadecimal']

# Populate the table with data from conversions
for i, (decimal, binary, hexadecimal) in enumerate(zip(decimals,
                                                       binaries,
                                                       hexadecimals)):
    results.add_row([i + 1, decimal, binary, hexadecimal])

# Print the table to the console
print(results)

# Calculate the total execution time of the script
execution_time = time.time() - start_time

# Print the execution time to the console
print(f'Execution time: {execution_time:.2f} seconds')

# Write the results and execution time to a text file
with open('ConvertionResults.txt', 'w', encoding='utf-8') as output:
    # Prepare the content to be written to the file
    output_content = f'{results}\nExecution time: {execution_time:.2f} seconds'
    # Write the content to the file
    output.write(output_content)
