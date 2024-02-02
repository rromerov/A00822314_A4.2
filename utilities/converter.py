"""
Utilities module for converting decimal numbers to binary and hexadecimal.
"""


class Converter:
    """
    Class for converting decimal numbers to binary and hexadecimal.
    """

    def __init__(self, data):
        # Initialize the Converter object with the provided data
        self.data = data

    def decimal_to_binary(self):
        """
        Convert the decimal numbers in the data to binary.
        If the element is not a number, it appends '#VALUE!' to the list.

        Returns:
            list: A list of binary numbers or #VALUE! for non-numeric elements.
        """
        # Initialize an empty list to store binary representations
        binary_list = []
        for item in self.data:
            # Check if the item is an integer
            if isinstance(item, int):
                # Check if the integer is negative
                if item < 0:
                    # Convert negative number to binary
                    binary_list.append(self._decimal_to_binary_negative(
                        item, 10)
                        )
                else:
                    # Convert positive number to binary
                    binary_list.append(self._decimal_to_binary_positive(item))
            else:
                # If the item is not an integer, append '#VALUE!'
                binary_list.append('#VALUE!')
        return binary_list

    def _decimal_to_binary_positive(self, num):
        """
        Convert a positive decimal number to binary.

        Args:
            num (int): The positive decimal number to be converted.

        Returns:
            str: The binary representation of the positive decimal number.
        """
        # Initialize an empty string to store the binary representation
        binary = ""
        while num > 0:
            # Add the remainder of num divided by 2 to the binary string
            binary = str(num % 2) + binary
            # Divide num by 2 and update its value
            num //= 2
        return binary if binary else "0"

    def _decimal_to_binary_negative(self, num, bits):
        """
        Convert a negative decimal number to binary using two's complement.

        Args:
            num (int): The negative decimal number to be converted.
            bits (int): The number of bits for the binary representation.

        Returns:
            str: The binary representation of the negative decimal number.
        """
        binary = ""
        # Convert negative number to positive for conversion
        num = (1 << bits) + num
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        return binary.zfill(bits)

    def decimal_to_hexadecimal(self):
        """
        Convert the decimal numbers in the data to hexadecimal.
        If the element is not a number, it appends '#VALUE!' to the list.

        Returns:
            list: A list of hexadecimal numbers or '#VALUE!' for non-numeric
            elements.
        """
        # Initialize an empty list to store hexadecimal representations
        hex_list = []
        for item in self.data:
            # Check if the item is an integer
            if isinstance(item, int):
                # Check if the integer is negative
                if item < 0:
                    # Convert negative number to hexadecimal
                    hex_list.append(self._decimal_to_hex_negative(item, 32))
                else:
                    # Convert positive number to hexadecimal.
                    hex_list.append(self._decimal_to_hex_positive(item))
            else:
                # If the item is not an integer, append '#VALUE!'
                hex_list.append('#VALUE!')
        return hex_list

    def _decimal_to_hex_positive(self, num):
        """
        Convert a positive decimal number to hexadecimal.

        Args:
            num (int): The positive decimal number.

        Returns:
            str: The hexadecimal representation of the positive decimal number.
        """
        # Define the characters used in hexadecimal representation
        hex_chars = "0123456789ABCDEF"
        # Initialize an empty string to store the hexadecimal representation
        hex_num = ""
        while num > 0:
            # Add the hexadecimal digit to the beginning of the string
            hex_num = hex_chars[num % 16] + hex_num
            # Divide num by 16 and update its value
            num //= 16
        return hex_num if hex_num else "0"

    def _decimal_to_hex_negative(self, num, bits):
        """
        Convert a negative decimal number to hexadecimal.

        Args:
            num (int): The negative decimal number.
            bits (int): The number of bits for representation.

        Returns:
            str: The hexadecimal representation of the negative decimal number.
        """
        # Convert negative number to positive for conversion
        num = (1 << bits) + num
        # Define the characters used in hexadecimal representation
        hex_chars = "0123456789ABCDEF"
        # Initialize an empty string to store the hexadecimal representation
        hex_num = ""
        while num > 0:
            # Add the hexadecimal digit to the beginning of the string
            hex_num = hex_chars[num % 16] + hex_num
            # Divide num by 16 and update its value
            num //= 16
        return hex_num.zfill(bits // 4)
