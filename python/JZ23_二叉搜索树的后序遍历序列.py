# 题目描述
# # 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。

class Solution:
    def VerifySquenceOfBST(self, sequence):

        if len(sequence) == 0:
            return False

        n = len(sequence)-1
        count = 0
        while n:
            while sequence[count] < sequence[n]:
                count += 1

            while sequence[count] > sequence[n]:
                count += 1

            if count < n:
                return False

            n -= 1
            count = 0

        return True

