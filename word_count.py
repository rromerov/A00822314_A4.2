"""
This module performs word counting on a list of strings and outputs
the results to a text file and the console.
"""
import time
from prettytable import PrettyTable
from utilities.data_loader import str_loader
from utilities.word_counter import WordCounter

start_time = time.time()

words = str_loader()

count_words = WordCounter(words)

results = PrettyTable()

results.field_names = ['Word', 'Count']

for word, count in count_words:
    results.add_row([word, count])

number_of_words = f'Grand Total {len(count_words)} words'

execution_time = f'Execution time: {time.time() - start_time:.6f} seconds'

end_result = f'{results}\n{number_of_words}\n{execution_time}'

print(end_result)

with open('WordCountResults.txt', 'w', encoding='utf-8') as output:
    output_content = end_result
    output.write(output_content)
