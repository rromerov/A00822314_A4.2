"""
Utilities module for converting decimal numbers to binary and hexadecimal.
"""


class Converter:
    """
    Class for converting decimal numbers to binary and hexadecimal.
    """

    def __init__(self, data):
        self.data = data

    def decimal_to_binary(self):
        """
        Convert the decimal numbers in the data to binary.
        If the element is not a number, it appends '#VALUE!' to the list.

        Returns:
            list: A list of binary numbers or #VALUE! for non-numeric elements.
        """
        binary_list = []
        for item in self.data:
            if isinstance(item, int):
                if item < 0:
                    binary_list.append(self._decimal_to_binary_negative(
                        item, 10)
                        )
                else:
                    binary_list.append(self._decimal_to_binary_positive(item))
            else:
                binary_list.append('#VALUE!')
        return binary_list

    def _decimal_to_binary_negative(self, num, bits):
        """
        Convert a negative decimal number to binary using two's complement.

        Args:
            num (int): The negative decimal number.
            bits (int): The number of bits for representation.

        Returns:
            str: The binary representation of the negative decimal number.
        """
        num = (1 << bits) + num
        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        return binary.zfill(bits)

    def _decimal_to_binary_positive(self, num):
        """
        Convert a positive decimal number to binary.

        Args:
            num (int): The positive decimal number.

        Returns:
            str: The binary representation of the positive decimal number.
        """
        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        return binary if binary else "0"

    def decimal_to_hexadecimal(self):
        """
        Convert the decimal numbers in the data to hexadecimal.
        If the element is not a number, it appends '#VALUE!' to the list.

        Returns:
            list: A list of hexadecimal numbers or '#VALUE!' for non-numeric
            elements.
        """
        hex_list = []
        for item in self.data:
            if isinstance(item, int):
                if item < 0:
                    hex_list.append(self._decimal_to_hex_negative(item, 32))
                else:
                    hex_list.append(self._decimal_to_hex_positive(item))
            else:
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
        hex_chars = "0123456789ABCDEF"
        hex_num = ""
        while num > 0:
            hex_num = hex_chars[num % 16] + hex_num
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
        num = (1 << bits) + num
        hex_chars = "0123456789ABCDEF"
        hex_num = ""
        while num > 0:
            hex_num = hex_chars[num % 16] + hex_num
            num //= 16
        return hex_num.zfill(bits // 4)
