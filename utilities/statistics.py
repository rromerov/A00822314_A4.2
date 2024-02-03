"""
Module containing a class for statistical operations.
"""


class Statistics:
    """
    A class for performing statistical operations on data.
    """

    def __init__(self, data):
        """
        Initialize the Statistics object with data.

        Args:
            data (list): A list of numeric data.
        """
        self.data = data

    def mean(self):
        """
        Calculate the mean of the data.

        Returns:
            float: The mean value of the data.
        """
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Calculate the median of the data.

        Returns:
            float: The median value of the data.
        """
        # Sort the data in ascending order
        sorted_data = sorted(self.data)
        # n = number of elements
        n = len(sorted_data)
        # If n is even, return the average of the middle 2 elements
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        # If n is odd, return the middle element
        return sorted_data[n//2]

    def mode(self):
        """
        Calculate the mode of the data.

        Returns:
            float or str: The mode of the data, or N/A if there is no mode.
        """
        # Create a dictionary to store the count of each unique element
        counts = {}
        for x in self.data:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        # Find the maximum count
        max_count = max(counts.values())

        # Find modes with the maximum count
        modes = [x for x, count in counts.items() if count == max_count]

        # If there is a single mode, return it
        if len(modes) == 1:
            return modes[0]

        # If there are 2 or more modes, return "N/A"
        return "N/A"

    def standard_deviation(self):
        """
        Calculate the standard deviation of the data.

        Returns:
            float: The standard deviation of the data.
        """
        # Calculate the mean of the data
        mean = self.mean()
        # Get the square root of the average of squared differences from mean
        return (sum((x - mean)**2 for x in self.data) / len(self.data))**0.5

    def variance(self):
        """
        Calculate the variance of the data.

        Returns:
            float: The variance of the data.
        """
        # Calculate the mean of the data
        mean = self.mean()
        # Calculate the average of squared differences from the mean
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)

    def valid_count(self):
        """
        Count the number of elements in the data.

        Returns:
            int: The number of elements in the data.
        """
        # Return the length of the data list
        return len(self.data)
