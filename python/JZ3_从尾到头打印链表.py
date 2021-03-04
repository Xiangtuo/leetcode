# 题目描述
# # 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):


    def printListFromTailToHead(self, listNode):

        if listNode == None:
            return []

        temp = pre = listNode

        while temp and temp.next:
            curr = temp.next
            temp.next = curr.next
            curr.next = pre
            pre = curr

        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next

        return res



