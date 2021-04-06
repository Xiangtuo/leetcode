# 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

class Solution:
    def Permutation(self, ss):
        res = []
        temp = ''
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        lens = len(ss)
        self.dfs(ss, temp, res, lens)
        return sorted(list(set(res)))

    def dfs(self, ss, temp, res, lens):
        if lens == len(temp):
            res.append(temp)
        for i in range(len(ss)):
            self.dfs(ss[:i] + ss[(i + 1):], temp + ss[i], res, lens)



