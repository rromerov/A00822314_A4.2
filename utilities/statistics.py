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
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        return sorted_data[n//2]

    def mode(self):
        """
        Calculate the mode of the data.

        Returns:
            float or str: The mode of the data, or N/A if there is no mode.
        """
        counts = {}
        for x in self.data:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        max_count = max(counts.values())
        modes = [x for x, count in counts.items() if count == max_count]

        if len(modes) == 1:
            return modes[0]
        if len(modes) > 1:
            return repr(modes)[1:-1].replace(',', '')
        return "N/A"

    def standard_deviation(self):
        """
        Calculate the standard deviation of the data.

        Returns:
            float: The standard deviation of the data.
        """
        mean = self.mean()
        return (sum((x - mean)**2 for x in self.data) / len(self.data))**0.5

    def variance(self):
        """
        Calculate the variance of the data.

        Returns:
            float: The variance of the data.
        """
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def valid_count(self):
        """
        Count the number of elements in the data.

        Returns:
            int: The number of elements in the data.
        """
        return len(self.data)
