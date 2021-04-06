# 题目描述
# 输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


import copy

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        temp = []
        val = expectNumber

        if root is None:
            return []

        self.dfs(root, expectNumber, res, temp, val)
        return res

    def dfs(self, root, expectNumber, res, temp, val):
        #         temp.append(root.val)
        if val == root.val and not root.left and not root.right:
            res.append(temp + [root.val])
        if root.left:
            self.dfs(root.left, expectNumber, res, temp + [root.val], val - root.val)
        if root.right:
            self.dfs(root.right, expectNumber, res, temp + [root.val], val - root.val)

    def dfs2(self, root, expectNumber, res, temp, val):
        temp.append(root.val)
        if val == root.val and not root.left and not root.right:
            key = copy.deepcopy(temp)
            res.append(key)
        if root.left:
            self.dfs(root.left, expectNumber, res, temp, val-root.val)
        if root.right:
            self.dfs(root.right, expectNumber, res, temp, val-root.val)
        temp.pop()




