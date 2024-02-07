"""
222. Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible.
It can have between one and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(self, root: Optional[TreeNode]) -> int:
    return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0
