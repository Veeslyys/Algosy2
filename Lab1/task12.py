def posled():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        a = list(map(int, file.readline().split()))

    totalsum = sum(a)

    if totalsum % 2 != 0:
        with open('output.txt', 'w') as outputfile:
            outputfile.write("-1")
        return

    target = totalsum // 2
    # Используем битовую маску для экономии памяти
    dp = 1  # Изначально можем набрать сумму 0

    elements = []
    for i in range(n):
        num = a[i]
        new_dp = dp | (dp << num)
        if new_dp != dp:
            elements.append((num, i + 1))
        dp = new_dp
        if (dp >> target) & 1:
            break

    if not ((dp >> target) & 1):
        with open('output.txt', 'w') as file:
            file.write("-1")
        return

    # Восстанавливаем подмножество
    current_sum = target
    subset = []
    for num, idx in reversed(elements):
        if current_sum >= num and (dp >> (current_sum - num)) & 1:
            subset.append(idx)
            current_sum -= num
            if current_sum == 0:
                break

    with open('output.txt', 'w') as outputfile:
        outputfile.write(f"{len(subset)}\n")
        outputfile.write(" ".join(map(str, sorted(subset))))


posled()
