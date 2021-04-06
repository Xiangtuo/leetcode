# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        stck = [root]
        res = []

        while len(stck):
            elem = stck.pop(0)
            res.append(elem.val)
            if elem.left:
                stck.append(elem.left)
            if elem.right:
                stck.append(elem.right)

        return res

