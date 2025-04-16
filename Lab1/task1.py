def fractional_knapsack():
    # Чтение входных данных с автоматическим закрытием файла
    with open('input.txt', 'r') as input_file:
        n, W = map(int, input_file.readline().split())
        items = []
        for i in range(n):
            p, w = map(int, input_file.readline().split())
            if w > 0:
                items.append((p, w, p / w))  # Кортеж из трёх элементов

    # Сортировка по убыванию удельной стоимости
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    remaining_weight = W

    # Жадный алгоритм
    for p, w, ratio in items:
        if remaining_weight <= 0:
            break
        take = min(w, remaining_weight)
        total_value += take * ratio
        remaining_weight -= take

    # Запись результата
    print(total_value, W, remaining_weight, items)
    with open('output.txt', 'w') as output_file:
        output_file.write('{0:.4f}'.format(total_value))


# Вызов функции
fractional_knapsack()