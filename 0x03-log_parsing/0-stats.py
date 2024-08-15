#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""

import sys
import re

file_size = 0
status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
line_number = 0
format_pattern = r'^[0-9\.]+\s-\s\[[0-9-]+\s[0-9:\.]+\]\s' +\
    r'"\w+\s\/projects\/260 HTTP\/1.1"\s[0-9]{3}\s[0-9]+$'

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
                for key in sorted(status_dict):
                    if status_dict[key] > 0:
                        print("{}: {}".format(key, status_dict[key]))
                line_number = 0

finally:
    print("File size: {}".format(file_size))
    for key in sorted(status_dict):
        if status_dict[key] > 0:
            print("{}: {}".format(key, status_dict[key]))
