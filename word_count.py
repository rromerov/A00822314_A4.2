"""
This module performs word counting on a list of strings and outputs
the results to a text file and the console.
"""
# Import libraries
import time
from prettytable import PrettyTable
from utilities.data_loader import word_data
from utilities.word_counter import WordCounter

# Start measuring the time before the operation begins
start_time = time.time()

# Initialize the word_data object to hold the words
words = word_data()

# Create an instance of WordCounter to count the words
count_words = WordCounter(words)

# Initialize a PrettyTable to display the results nicely
results = PrettyTable()

# Set the field names for the PrettyTable
results.field_names = ['Word', 'Count']

# Add the word counts to the PrettyTable
for word, count in count_words:
    results.add_row([word, count])

# Create a string indicating the total number of words counted.
number_of_words = f'Grand Total {len(count_words)} words'

# Calculate the execution time and format it.
execution_time = f'Execution time: {time.time() - start_time:.6f} seconds'

# Combine the PrettyTable, total word count, and execution time
end_result = f'{results}\n{number_of_words}\n{execution_time}'

# Print the final result.
print(end_result)

# Write the final result to a text file named WordCountResults.txt
with open('WordCountResults.txt', 'w', encoding='utf-8') as output:
    output.write(end_result)
