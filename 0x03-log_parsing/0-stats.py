#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""

import sys
import re

file_size = 0
status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
line_number = 0
format_pattern = format_pattern = r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\s-\s\[' +\
    r'[0-9]{2}/[A-Za-z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}\s' +\
    r'\+\d{4}\]\s"\w+\s\/projects\/260\sHTTP\/1.1"\s[0-9]{3}\s[0-9]+$'

try:
    for line in sys.stdin:
        line = line.strip()
        line_parts = line.split()
        if re.match(format_pattern, line):

            status_code = line_parts[7]
            if status_code in status_dict:
                status_dict[status_code] += 1
            try:
                file_size += int(line_parts[8])
            except Exception:
                pass
            line_number += 1

            if line_number == 10:
                print("File size: {}".format(file_size))
                for key, value in sorted(status_dict.items()):
                    if value > 0:
                        print("{}: {}".format(key, value))
                line_number = 0

except KeyboardInterrupt:
    pass

print("File size: {}".format(file_size))
for key, value in sorted(status_dict.items()):
    if value > 0:
        print("{}: {}".format(key, value))
