
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

    solution1 = 0

    for update in updates:
        valid_flag = True
        for idx, first_page in enumerate(update):
            if not valid_flag:
                break
            for second_page in update[idx+1:]:
                if second_page not in ordering_rules_dict.get(first_page, []):
                    valid_flag = False
                    break
        if valid_flag:
            solution1 += update[len(update) // 2]


    print(solution1)