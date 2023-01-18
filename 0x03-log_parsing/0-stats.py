#!/usr/bin/python3
"""0-stats.py"""

import sys

code_status = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_sizes = 0
count_line = 1


def printStats():
    """Print the final statistics after all lines have been read"""
    print('File size: {}'.format(total_sizes))
    for code in sorted(code_status.keys()):
        if code_status[code] != 0:
            print('{}: {}'.format(code, code_status[code]))


try:
    for line in sys.stdin:
        try:
            line = line[:-1]
            parts = line.split(' ')
            total_sizes += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in code_status:
                code_status[status_code] += 1
        except Exception:
            pass

        if count_line % 10 == 0:
            printStats()
        count_line += 1

except KeyboardInterrupt:
    printStats()
    raise

printStats()
