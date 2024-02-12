"""
Given 2 arrays representing a graph, return True if the following requirement is existing:
1. all nodes in the graph are connected
2. all nodes are one big circle.
 example:
 input: arr_1 = [1,2,3]     arr_2 = [2,3,1]
 output: True
 explained: arr_1[0] == 1  connected to arr_2[0] == 2 meaning node 1 connected to mode 2          1
          arr_1[1] == 2  connected to arr_2[1] == 3 meaning node 2 connected to mode 3          /  \
          arr_1[2] == 1  connected to arr_2[2] == 1 meaning node 3 connected to mode 1         3 _ 2
*** all nodes are bidirectional meaning that if node 1 connected to mode 2 also, meaning node 2 connected to mode 1.
"""


def graph_is_circle(arr_1, arr_2):
    pass

