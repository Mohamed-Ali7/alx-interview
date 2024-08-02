#!/usr/bin/python3
"""This modules contains canUnlockAll() function"""


def canUnlockAll(boxes: list):
    """Returns True if all boxes can be opened, else return False"""

    n = boxes.__len__()
    result = True
    boxes_status_dict = {key: False for key in range(n)}
    boxes_status_dict[0] = True
    boxes_status_array = []

    for i in range(n):
        box = boxes[i]
        for key in box:
            if key == i or key >= n:
                continue
            boxes_status_dict[key] = True

    boxes_status_array = boxes_status_dict.values()

    for box_status in boxes_status_array:
        if not box_status:
            return False
    return result
