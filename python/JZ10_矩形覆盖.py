# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#
# 比如n=3时，2*3的矩形块有3种覆盖方法：


class Solution(object):
    def rectCover(self, number):

        dp = [0 for _ in range((number+1))]

        if number <= 1:
            return number

        dp[1] = dp[0] = 1

        for i in range(2, number+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[number]


