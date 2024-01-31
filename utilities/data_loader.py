"""
Module to load data from a text file.
"""

import sys


def txt_loader():
    """
    Loads numeric data from a text file provided as a command-line argument.

    Returns:
        list: A list containing the numeric data.
    """
    if len(sys.argv) < 2:
        print('No file name given. To run the script, type: python'
              'compute_statistics.py <fileName.txt>')
        sys.exit(1)

    file = sys.argv[1]
    numbers = []
    with open(file, 'r', encoding='utf-8') as processed_file:
        for line in processed_file:

            # Remove the new line character
            line = line.strip()

            try:
                # Convert the string to a float
                value = float(line)
            except ValueError:
                # If the string can't be converted to a float, ignore it
                print(f'The following element is not a number: {line}')
                continue

            # Add the number to the list
            numbers.append(value)
    return numbers


def int_loader():
    """
    Loads integer data from a text file provided as a command-line argument.

    Returns:
        list: A list containing the integer data.
    """
    if len(sys.argv) < 2:
        print('No file name given. To run the script, type: python'
              'convert_numbers.py <fileName.txt>')
        sys.exit(1)

    file = sys.argv[1]
    numbers = []
    with open(file, 'r', encoding='utf-8') as processed_file:
        for line in processed_file:

            # Remove the new line character
            line = line.strip()

            try:
                # Convert the string to an integer
                value = int(line)
            except ValueError:
                # If the string can't be converted to an integer, ignore it
                print(f'The following element is not a number: {line}')
                value = line

            # Add the number to the list
            numbers.append(value)
    return numbers
