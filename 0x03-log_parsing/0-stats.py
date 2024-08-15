#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""

import sys
import re

file_size = 0
status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
line_number = 0
format_pattern = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

try:
    for line in sys.stdin:
        line_parts = line.split()
        if format_pattern.fullmatch(line):

            status_code = line_parts[7]
            if status_code in status_dict:
                status_dict[status_code] += 1

            file_size += int(line_parts[8])
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
