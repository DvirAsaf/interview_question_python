import collections


def reachable_node(arr):
    graph = collections.defaultdict(list)
    for a, b in arr:
        graph[a].append(b)
        graph[b].append(a)

    print(graph)
    inter = []
    for val in graph.values():
        if not inter:
            inter = val
        else:
            inter = set(val) & set(inter)

    print("inter", inter)


if __name__ == '__main__':
    arr = [[1, 2], [2, 3], [4, 2]]
    reachable_node(arr)