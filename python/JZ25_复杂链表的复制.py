# 题目描述
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):

        p1 = p2 = pHead
        nodes = []
        dict = {}

        while p1:
            nodes.append(p1)
            p1 = p1.next

        while p2:
            if p2.random:
                dict[nodes.index(p2)] = nodes.index(p2.random)
            else:
                dict[nodes.index(p2)] = -1

            p2 = p2.next

        new_node = [RandomListNode(x.label) for x in nodes]

        for i, node in enumerate(new_node):
            if i < len(new_node)-1:
                node.next = new_node[i+1]
            if dict[i] != -1:
                node.random = new_node[dict[i]]

        return new_node[0]



