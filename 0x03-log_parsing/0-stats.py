#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""

import sys
import re

file_size = 0
status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
line_number = 1
format_pattern = r'^[0-9\.]+\s-\s\[[0-9-]+\s[0-9:\.]+\]\s' +\
    r'"\w+\s\/projects\/260 HTTP\/1.1"\s[0-9]{3}\s[0-9]+$'

try:
    for line in sys.stdin:
        if re.search(format_pattern, line.strip()):
            status_dict[line.split()[7]] += 1
            file_size += int(line.split()[8])
            if line_number == 10:
                print(f"File size: {file_size}")
                for key, value in status_dict.items():
                    if value > 0:
                        print(f"{key}: {value}")
                        line_number = 1
            line_number += 1

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key, value in status_dict.items():
        if value > 0:
            print(f"{key}: {value}")