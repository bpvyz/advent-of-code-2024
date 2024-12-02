with open('input.txt', 'r') as f:
    lines = f.readlines()
    solution1 = 0
    for line in lines:
        report = list(map(int, line.split()))
        safe = lambda report: (
                all(1 <= y - x <= 3 for x, y in zip(report, report[1:])) or
                all(1 <= x - y <= 3 for x, y in zip(report, report[1:]))
        )
        if(safe(report)):
            solution1 += 1

    print(solution1)