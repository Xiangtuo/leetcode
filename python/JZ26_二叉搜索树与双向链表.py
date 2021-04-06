# 题目描述
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.head = None
        self.pre = None
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return
        self.Convert(pRootOfTree.left)
        if self.head is None:
            self.head = pRootOfTree
        pRootOfTree.left = self.pre
        if self.pre is not None:
            self.pre.right = pRootOfTree
        self.pre = pRootOfTree
        self.Convert(pRootOfTree.right)

        return self.head

