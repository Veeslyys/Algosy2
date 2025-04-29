import sys
from collections import deque


def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr + 1])
    ptr += 2

    edges = []
    for i in range(m):
        u = int(input[ptr])
        v = int(input[ptr + 1])
        w = int(input[ptr + 2])
        edges.append((u, v, w))
        ptr += 3

    s = int(input[ptr])

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0

    for i in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    on_negative_cycle = [False] * (n + 1)

    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            on_negative_cycle[v] = True

    if any(on_negative_cycle):
        reverse_edges = [[] for _ in range(n + 1)]
        for u, v, _ in edges:
            reverse_edges[v].append(u)

        visited = [False] * (n + 1)
        q = deque()

        for v in range(1, n + 1):
            if on_negative_cycle[v] and not visited[v]:
                q.append(v)
                visited[v] = True

        while q:
            u = q.popleft()
            for v in reverse_edges[u]:
                if not visited[v]:
                    visited[v] = True
                    on_negative_cycle[v] = True
                    q.append(v)

    for v in range(1, n + 1):
        if dist[v] == INF:
            print("*")
        elif on_negative_cycle[v]:
            print("-")
        else:
            print(dist[v])

main()