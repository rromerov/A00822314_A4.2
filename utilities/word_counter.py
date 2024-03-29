"""
Utilities module for counting words in a list of strings.
"""


class WordCounter:
    """
    Utility class for counting words in a list of strings.

    Args:
        data (list): A list of strings.

    Attributes:
        data (list): A list of strings containing words.

    Methods:
        count_words: Counts the occurrences of each word in the provided list.
        __iter__: Iterator method to iterate over the word counts.
        __len__: Returns the total number of words in the WordCounter.
    """

    def __init__(self, data):
        """
        Initializes the WordCounter with the provided list of strings.

        Args:
            data (list): A list of strings containing words.
        """
        self.data = data

    def count_words(self):
        """
        Counts the occurrences of each word in the provided list.

        Returns:
            dict: A dictionary where keys are words and values are their
            counts.
        """
        # Initialize an empty dictionary to store the word count
        word_count = {}
        # Iterate over each word in the provided list
        for word in self.data:
            # Increase the count of the current word in the word_count dict
            word_count[word] = word_count.get(word, 0) + 1
        # Return the resulting word count dictionary
        return word_count

    def __iter__(self):
        """
        Iterator method to iterate over the word counts.
        """
        return iter(self.count_words().items())

    def __len__(self):
        """
        Returns the total number of words in the WordCounter.
        """
        return sum(self.count_words().values())
