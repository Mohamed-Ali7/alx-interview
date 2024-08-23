#!/usr/bin/python3
"""This module contains valudUTF8() function"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    def validateBytes(start, n):
        """Helper function to check if the data is a valid UTF-8 encoding."""
        for i in range(start + 1, start + n + 1):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        if data[i] >> 7 == 0:
            i += 1
        elif data[i] >> 5 == 0b110 and validateBytes(i, 1):
            i += 2
        elif data[i] >> 4 == 0b1110 and validateBytes(i, 2):
            i += 3
        elif data[i] >> 3 == 0b11110 and validateBytes(i, 3):
            i += 4
        else:
            return False

    return True
