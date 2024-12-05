import re

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    solution1 = 0

    words_found = 0
    word = "XMAS"
    search = re.compile(r'XMAS')

    transposed = ["".join(row[i] for row in lines) for i in range(len(lines[0]))]
    diagonals = []

    rows, cols = len(lines), len(lines[0])
    # main diagonal
    for d in range(-(rows - 1), cols):
        diagonals.append("".join(lines[i][i - d] for i in range(max(0, d), min(rows, cols + d))))
    # secondary diagonal
    for d in range(rows + cols - 1):
        diagonals.append("".join(lines[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))))

    # horizontal search
    for line in lines:
        words_found += len(search.findall(line))
        words_found += len(search.findall(line[::-1]))

    # vertical search
    for line in transposed:
        words_found += len(search.findall(line))
        words_found += len(search.findall(line[::-1]))

    # diagonal search
    for line in diagonals:
        words_found += len(search.findall(line))
        words_found += len(search.findall(line[::-1]))

    solution1 = words_found

    print(solution1)
