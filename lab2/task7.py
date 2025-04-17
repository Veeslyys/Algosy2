def is_bst(tree, root_idx=0):
    stack = []
    prev = None
    current = root_idx

    while stack or current != -1:
        while current != -1:
            stack.append(current)
            current = tree[current][1]  # к левому ребенку

        current = stack.pop()
        # Проверяем, что текущий ключ больше предыдущего
        if prev is not None and tree[current][0] < prev:
            return False
        prev = tree[current][0]
        current = tree[current][2]  # к правому ребенку

    return True


def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        if n == 0:
            with open('output.txt', 'w') as out_f:
                out_f.write("CORRECT")
                print('CORRECT')
            return

        tree = []
        for _ in range(n):
            K, L, R = map(int, f.readline().split())
            tree.append((K, L, R))

    if is_bst(tree):
        result = "CORRECT"
    else:
        result = "INCORRECT"

    print(result)

main()