list1 = []
list2 = []
solution2 = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    pairs = list(map(lambda x: x.strip().split("   "), lines))
    list1 = list(map(lambda y: int(y[0]), pairs))
    list2 = list(map(lambda z: int(z[1]), pairs))

    solution2 += sum(map(lambda i: i * list2.count(i), list1))

    print(solution2)