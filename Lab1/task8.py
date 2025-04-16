def max_lectures(N, lectures):
    # Сортируем лекции по времени окончания
    lectures.sort(key=lambda x: x[1])
    count = 0
    last_end = 0
    for s, f in lectures:
        if s >= last_end:
            count += 1
            last_end = f
    return count
# Чтение входных данных
with open('input.txt', 'r') as f:
    N = int(f.readline())
    lectures = []
    for _ in range(N):
        s, f = map(int, f.readline().split())
        lectures.append((s, f))
# Вычисление результата
result = max_lectures(N, lectures)
# Запись результата
with open('output.txt', 'w') as f:
    f.write(str(result))