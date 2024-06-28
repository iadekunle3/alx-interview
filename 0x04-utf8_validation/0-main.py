#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0b-validate_utf8').validUTF8

data = [223, 65, 127, 256]
print(validUTF8(data))

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))



data = [226, 130, 172]
print(validUTF8(data))

data = [229, 173, 151]
print(validUTF8(data))