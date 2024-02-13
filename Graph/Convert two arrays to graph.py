import collections


# this is for undirected graph
def convert_two_arrays_to_undirected_graph(arr1, arr2):
    graph = collections.defaultdict(list)
    # n = len(arr1)
    # for i in range(n):
    #     graph[arr1[i]].append(arr2[i])
    # for j in range(n):
    #     graph[arr2[j]].append(arr1[j])
    for elem1, elem2 in zip(arr1, arr2):
        graph[elem1].append(elem2)
        graph[elem2].append(elem1)

    print(graph)


# this is for directed graph
def convert_two_arrays_to_directed_graph(arr1, arr2):
    graph = collections.defaultdict(list)
    # n = len(arr1)
    # for i in range(n):
    #     graph[arr1[i]].append(arr2[i])
    for elem1, elem2 in zip(arr1, arr2):
        graph[elem1].append(elem2)

    print(graph)


if __name__ == '__main__':
    arr1 = [1, 1, 4, 3]
    arr2 = [2, 3, 2, 4]
    convert_two_arrays_to_undirected_graph(arr1, arr2)
    convert_two_arrays_to_directed_graph(arr1, arr2)
