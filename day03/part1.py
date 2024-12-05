import re
from functools import reduce
from operator import mul

with open('input.txt', 'r') as f:
    lines = f.readlines()
    solution1 = 0
    muls = []
    for line in lines:
        muls += re.findall(r'mul\(\d+,\d+\)', line)
    for elem in muls:
        solution1 += reduce(mul, list(map(int, elem[4:-1].split(','))))

    print(solution1)