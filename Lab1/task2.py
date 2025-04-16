def refuel_count():
    with open('pumpumpum.txt', 'r') as file:
        d = int(file.readline())
        m = int(file.readline())
        n = int(file.readline())
        refuels = [0] + list(map(int, file.readline().split())) + [d]
    num_refuels = 0
    curent_refuel = m
    for i in range(1, len(refuels)):
        dist = refuels[i] - refuels[i-1]
        if dist > m:
            with open('output.txt', 'w') as output_file:
                output_file.write('-1')
            return
        if curent_refuel < dist:
            curent_refuel = m
            num_refuels += 1
        curent_refuel -= dist
    with open('output.txt', 'w') as output_file:
        output_file.write(str(num_refuels))
refuel_count()



