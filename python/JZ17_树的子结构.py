# 题目描述
# # 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):

        if pRoot1 is None or pRoot2 is None:
            return False

        return self.dfs(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def dfs(self, p1, p2):
        if p2 is None:
            return True
        if p1 is None:
            return False

        return p1.val == p2.val and self.dfs(p1.left, p2.left) and self.dfs(p1.right, p2.right)

