#!/usr/bin/python3

"""
This module loops through standard input for specific formats
"""

import sys
import re
import signal


def print_stats(total_size, status_codes, status_code_count):
    """
    Function that prints saved stats
    """

    print(f"File size {total_size}")

    for index, code in enumerate(status_codes):
        print(f"{code}: {status_code_count[index]}")


def main():
    """
    Main part of module that loops
    """

    # must \ periods and square brackets
    # ? means the group doesn't have to be there
    # ^ means it must match the start of a line
    input_format1 = r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} '
    input_format2 = r'\d{2}:\d{2}:\d{2}(\.\d{1,6})?\] '
    input_format3 = r'"GET /projects/260 HTTP/1\.1" \d{3} \d{1,4}$'
    input_format = input_format1 + input_format2 + input_format3
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_code_count = [0] * 8
    total_size = 0
    files_read = 0

    try:
        for line in sys.stdin:

            stripped_line = line.strip()
            # strip removes leading and trailing spaces
            if re.fullmatch(input_format, line.strip()):
                # Add file size
                file_size = stripped_line.split(" ")[-1]
                total_size += int(file_size)

                # Add status code
                status_code = stripped_line.split(" ")[-2]
                for index, code in enumerate(status_codes):
                    try:
                        if int(status_code) == code:
                            status_code_count[index] += 1
                    except ValueError:
                        pass

            files_read += 1

            if files_read != 0 and files_read % 10 == 0:
                print_stats(total_size, status_codes, status_code_count)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes, status_code_count)

    if __name__ == "__main__":
        main()
