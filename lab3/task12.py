import sys
from collections import defaultdict


def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    m = int(data[ptr + 1])
    ptr += 2

    graph = defaultdict(dict)

    for i in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        c = int(data[ptr + 2])
        ptr += 3
        graph[u][c] = v
        graph[v][c] = u

    k = int(data[ptr])
    ptr += 1

    if k == 0:
        print(1)
        return

    path = list(map(int, data[ptr:ptr + k]))

    current = 1
    for color in path:
        if color not in graph[current]:
            print("INCORRECT")
            return
        current = graph[current][color]

    print(current)


main()