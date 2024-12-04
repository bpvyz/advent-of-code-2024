with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    solution1 = 0

    for idx, line in enumerate(lines):
        for idx_l, letter in enumerate(line):
            if letter == 'A' and len(lines) > idx > 0 and len(line) > idx_l > 0:
                try:
                    top_left, top_right = lines[idx-1][idx_l-1], lines[idx-1][idx_l+1]
                    bottom_left, bottom_right = lines[idx+1][idx_l-1], lines[idx+1][idx_l+1]
                except IndexError:
                    continue
                try:
                    if (top_left == 'M' and
                        bottom_right == 'S' and
                        top_right == 'M' and
                        bottom_left == 'S'):
                        solution1 += 1
                        continue
                    elif (top_left == 'M' and
                          bottom_right == 'S' and
                          bottom_left == 'M' and
                          top_right == 'S'):
                        solution1 += 1
                        continue
                    elif (bottom_right == 'M' and
                          top_left == 'S' and
                          top_right == 'M' and
                          bottom_left == 'S'):
                        solution1 += 1
                        continue
                    elif (bottom_right == 'M' and
                          top_left == 'S' and
                          bottom_left == 'M' and
                          top_right == 'S'):
                        solution1 += 1
                        continue
                except IndexError:
                    pass

    print(solution1)
