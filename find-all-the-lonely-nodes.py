"""
1469. find-all-the-lonely-nodes
In a binary tree, a lonely node is a node that is the only child of its parent node.
The root of the tree is not lonely because it does not have a parent node.
Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree.
Return the list in any order.
Example 1:
Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.
Example 2:
Input: root = [7, 1, 4, 6, null, 5, 3, null,null,null,null,null,2]
Output: [6,2]
Explanation: Light blue nodes are lonely nodes.
Please remember that order doesn't matter, [2,6] is also an acceptable answer.
"""
from typing import Optional, List

from countNodes import TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_lonely_nodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return
            if root.left and not root.right:
                ans.append(root.left.val)
            elif root.right and not root.left:
                ans.append(root.right.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans
