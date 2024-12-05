with open('input.txt', 'r') as f:
    lines = f.readlines()
    solution2 = 0
    for line in lines:
        report = list(map(int, line.split()))
        safe = lambda report: (
                all(1 <= y - x <= 3 for x, y in zip(report, report[1:])) or
                all(1 <= x - y <= 3 for x, y in zip(report, report[1:]))
        )
        if(safe(report)):
            solution2 += 1
        else:
            unsafe_count = 0
            for i in range(len(report)):
                modified = report[:i] + report[i+1:]
                if safe(modified):
                    solution2 += 1
                    break
                elif unsafe_count == len(report)-1:
                    break
                else:
                    unsafe_count += 1

    print(solution2)
