
list1 = []
list2 = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    pairs = list(map(lambda x: x.strip().split("   "), lines))
    list1 = sorted(list(map(lambda y: int(y[0]), pairs)))
    list2 = sorted(list(map(lambda z: int(z[1]), pairs)))

    solution1 = sum([abs(x-y) for x, y in zip(list1, list2)])

    print(solution1)