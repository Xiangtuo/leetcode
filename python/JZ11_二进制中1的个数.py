# 题目描述
# 输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。


class Solution(object):
    def NumberOf1(self, n):

        count = 0

        if n < 0:
            n = n & 0xffffffff

        while n:
            count += 1
            n = n & (n-1)

        return count


if __name__ == '__main__':
    n = -1
    print(bin(n))
    m = n & 0xffffffff
    print(bin(m))


