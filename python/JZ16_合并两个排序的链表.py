# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

        dummpy = ListNode(-1)
        res = dummpy

        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                dummpy.next = pHead1
                pHead1 = pHead1.next
            elif pHead1.val > pHead2.val:
                dummpy.next = pHead2
                pHead2 = pHead2.next
            dummpy = dummpy.next

        while pHead1:
            dummpy.next = pHead1
            pHead1 = pHead1.next
            dummpy = dummpy.next

        while pHead2:
            dummpy.next = pHead2
            pHead2 = pHead2.next
            dummpy = dummpy.next

        return res.next



