def solve_apples():
    with open('input.txt', 'r') as file:
        n, s = map(int, file.readline().split())
        apples = []
        for i in range(n):
            a, b = map(int, file.readline().split())
            apples.append((a, b, i + 1))  # храним ai, bi и номер яблока

    # Разделяем яблоки на две группы:
    # 1. Те, где bi >= ai (выгодные - дают в итоге прирост)
    # 2. Те, где bi < ai (опасные - дают в итоге уменьшение)
    group1 = []
    group2 = []

    for a, b, idx in apples:
        if b >= a:
            group1.append((a, b, idx))
        else:
            group2.append((a, b, idx))

    # Сортируем группу 1 по возрастанию ai (сначала те, что меньше уменьшают)
    group1.sort(key=lambda x: x[0])

    # Сортируем группу 2 по убыванию bi (сначала те, что больше увеличивают)
    group2.sort(key=lambda x: -x[1])

    # Пытаемся съесть яблоки в порядке: group1, затем group2
    current_height = s
    order = []

    for a, b, idx in group1 + group2:
        current_height -= a
        if current_height <= 0:
            with open('output.txt', 'w') as file:
                file.write("-1")
            return
        current_height += b
        order.append(idx)

    # Если дошли до конца - выводим порядок
    with open('output.txt', 'w') as file:
        file.write(" ".join(map(str, order)))


solve_apples()