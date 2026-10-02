#!/usr/bin/python3

def pascal_triangle(n):
    lines = []
    if n <= 0:
        return lines
    if n == 1:
        lines = [[1]]
        return lines
    if n == 2:
        lines = [[1], [1, 1]]
        return lines
    lines = lines + pascal_triangle(n - 1)
    current_line = []
    for i in range(1, n):
        if i == 1:
            current_line.append(1)
        current_line.append(lines[n - 2][i - 1] + lines[n - 2][i - 2])
    current_line.append(1)
    lines.append(current_line)
    return lines
