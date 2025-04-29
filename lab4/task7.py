import sys


def solve():
    input = sys.stdin.read().split('\n')
    for line in input:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 2:
            continue
        s, t = parts
        find_lcs(s, t)


def find_lcs(s, t):
    n, m = len(s), len(t)
    if n == 0 or m == 0:
        print(0, 0, 0)
        return

    base = 911382629
    mod1 = 10 ** 18 + 3
    mod2 = 10 ** 18 + 7
    best_len = 0
    pos_s, pos_t = 0, 0

    low, high = 1, min(n, m)

    while low <= high:
        mid = (low + high) // 2
        found = False
        hash_map = {}

        max_pow1 = pow(base, mid - 1, mod1)
        max_pow2 = pow(base, mid - 1, mod2)
        h1, h2 = 0, 0

        for i in range(mid):
            h1 = (h1 * base + ord(s[i])) % mod1
            h2 = (h2 * base + ord(s[i])) % mod2
        hash_map[(h1, h2)] = 0

        for i in range(mid, n):
            h1 = (h1 - ord(s[i - mid]) * max_pow1) % mod1
            h2 = (h2 - ord(s[i - mid]) * max_pow2) % mod2
            h1 = (h1 * base + ord(s[i])) % mod1
            h2 = (h2 * base + ord(s[i])) % mod2
            hash_map[(h1, h2)] = i - mid + 1

        h1, h2 = 0, 0
        for i in range(mid):
            h1 = (h1 * base + ord(t[i])) % mod1
            h2 = (h2 * base + ord(t[i])) % mod2

        if (h1, h2) in hash_map:
            start_s = hash_map[(h1, h2)]
            if s[start_s:start_s + mid] == t[:mid]:
                found = True
                pos_s, pos_t = start_s, 0

        if not found:
            for i in range(mid, m):
                h1 = (h1 - ord(t[i - mid]) * max_pow1) % mod1
                h2 = (h2 - ord(t[i - mid]) * max_pow2) % mod2
                h1 = (h1 * base + ord(t[i])) % mod1
                h2 = (h2 * base + ord(t[i])) % mod2

                if (h1, h2) in hash_map:
                    start_s = hash_map[(h1, h2)]
                    start_t = i - mid + 1
                    if s[start_s:start_s + mid] == t[start_t:start_t + mid]:
                        found = True
                        pos_s, pos_t = start_s, start_t
                        break

        if found:
            best_len = mid
            low = mid + 1
        else:
            high = mid - 1

    if best_len == 0:
        print(0, 0, 0)
    else:
        print(pos_s, pos_t, best_len)


solve()