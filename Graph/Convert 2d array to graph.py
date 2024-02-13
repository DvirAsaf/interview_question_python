import collections


def convert_2d_array_to_undirected_graph(arr):
    graph = collections.defaultdict(list)
    for elem1, elem2 in arr:
        graph[elem1].append(elem2)
        graph[elem2].append(elem1)

    print(graph)


def convert_2d_array_to_directed_graph(arr):
    graph = collections.defaultdict(list)
    for elem1, elem2 in arr:
        graph[elem1].append(elem2)

    print(graph)


if __name__ == '__main__':
    arr = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
    convert_2d_array_to_undirected_graph(arr)
    arr = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
    convert_2d_array_to_directed_graph(arr)
