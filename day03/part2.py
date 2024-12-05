import re
from functools import reduce
from operator import mul

with open('input.txt', 'r') as f:
    lines = f.read()

mul_pattern = re.compile(r'mul\(\d+,\d+\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")

muls = [(match.group(), match.start()) for match in mul_pattern.finditer(lines)]

commands = []
for match in do_pattern.finditer(lines):
    commands.append((1, match.start()))
for match in dont_pattern.finditer(lines):
    commands.append((0, match.start()))

commands.sort(key=lambda x: x[1])

current_state = 1
last_command_position = -1
solution2 = 0

for mul_match, mul_pos in muls:

    while commands and commands[0][1] < mul_pos:
        current_state = commands.pop(0)[0]
        last_command_position = mul_pos

    if current_state == 1:
        numbers = list(map(int, mul_match[4:-1].split(',')))
        solution2 += reduce(mul, numbers)

print(solution2)
