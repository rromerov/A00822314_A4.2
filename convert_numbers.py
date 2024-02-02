"""
Module to convert decimal numbers to binary and hexadecimal from a text file.
"""
import time
from prettytable import PrettyTable
from utilities.data_loader import converter_data
from utilities.converter import Converter

start_time = time.time()

decimals = converter_data()

conversions = Converter(decimals)

binaries = conversions.decimal_to_binary()

hexadecimals = conversions.decimal_to_hexadecimal()

results = PrettyTable()

results.field_names = ['Number', 'Decimal', 'Binary', 'Hexadecimal']

for i, (decimal, binary, hexadecimal) in enumerate(
    zip(decimals, binaries, hexadecimals)
):
    results.add_row([i + 1, decimal, binary, hexadecimal])

print(results)

execution_time = time.time() - start_time

print(f'Execution time: {execution_time:.2f} seconds')

with open('ConvertionResults.txt', 'w', encoding='utf-8') as output:
    output_content = f'{results}\nExecution time: {execution_time:.2f} seconds'
    output.write(output_content)
