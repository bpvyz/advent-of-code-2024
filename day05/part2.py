
with open('input.txt', 'r') as f:
    lines = f.read().split("\n")
    ordering_rules = lines[:lines.index('')]
    updates = lines[lines.index('')+1:]
    ordering_rules_dict = {}

    for idx in range(len(updates)):
        updates[idx] = list(map(int, updates[idx].split(',')))

    for elem in ordering_rules:
        pages = elem.split('|')
        first_page, second_page = int(pages[0]), int(pages[1])
        if first_page in ordering_rules_dict:
            ordering_rules_dict[first_page].append(second_page)
        else:
            ordering_rules_dict[first_page] = [second_page]

    solution2 = 0

    for update in updates:
        idx = 0
        incorrect = False
        while idx < len(update):
            first_page = update[idx]
            retry = False
            for idx_s in range(idx+1, len(update)):
                second_page = update[idx_s]
                if second_page not in ordering_rules_dict.get(first_page, []):
                    update[idx], update[idx_s] = update[idx_s], update[idx]
                    retry = True
                    incorrect = True
                    break
            if retry:
                continue
            idx += 1
        if incorrect:
            solution2 += update[len(update) // 2]

    print(solution2)