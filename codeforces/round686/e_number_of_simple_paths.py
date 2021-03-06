import queue


def number_of_simple_path(g, n):
    leafs = queue.Queue()
    for i in range(n):
        if len(g[i]) == 1:
            leafs.put(i)

    val = [1] * n
    while leafs.empty() != True:
        v = leafs.get()
        to = g[v].pop()
        val[to] += val[v]
        val[v] = 0
        g[v].clear()
        g[to].remove(v)
        if len(g[to]) == 1:
            leafs.put(to)

    res = 0
    for i in range(n):
        val_i = val[i]
        res += val_i * (val_i - 1) // 2 + val_i * (n - val_i)

    return res


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        g = [set() for _ in range(n)]
        for j in range(n):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            g[x].add(y)
            g[y].add(x)

        n_path = number_of_simple_path(g, n)
        print(n_path)


if __name__ == '__main__':
    main()
