"""
Module to load data from a text file.
"""

import sys


def stadistic_data():
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
    not_numbers = []
    try:
        with open(file, 'r', encoding='utf-8') as processed_file:
            for line in processed_file:

                # Remove the new line character
                line = line.strip()

                try:
                    # Convert the string to a float if possible
                    value = float(line)
                    numbers.append(value)

                except ValueError:
                    # If the string can't be converted to a float, ignore it
                    not_numbers.append(line)
                    print(f'The following element is not a number: {line}')
                    continue
    except FileNotFoundError:
        print(f'Error: File "{file}" not found.')
        sys.exit(1)

    return numbers, not_numbers


def converter_data():
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
    try:
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
    except FileNotFoundError:
        print(f'Error: File "{file}" not found.')
        sys.exit(1)

    return numbers


def word_data():
    """
    Loads data from a text file.

    Args:
        file_name (str): Name of the text file.

    Returns:
        list: A list containing valid strings from the file.
    """
    if len(sys.argv) < 2:
        print('No file name given. To run the script, type: python'
              'word_count.py <fileName.txt>')
        sys.exit(1)

    file = sys.argv[1]
    words = []
    try:
        with open(file, 'r', encoding='utf-8') as processed_file:
            for line_number, line in enumerate(processed_file, start=1):
                # Remove the new line character and trailing whitespaces
                line = line.strip()

                # Check if line is empty after stripping
                if not line:
                    print(f'Warning: Empty line found at line {line_number}')
                    continue

                # Add the string to the list
                words.append(line)
    except FileNotFoundError:
        print(f'Error: File "{file}" not found.')
        sys.exit(1)

    return words
