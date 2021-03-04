# 题目描述:
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution(object):

    def Find1(self, target, array):
        for elem in array:
            if target in elem:
                return True

        return False

    def Find2(self, target, array):
        rows = len(array)
        cols = len(array[0])

        if rows == 0 or cols == 0:
            return False

        row = rows - 1
        col = 0

        while row >= 0 and col < cols:
            if array[row][col] < target:
                col = col + 1
            elif array[row][col] > target:
                row = row - 1
            else:
                return True

        return False


if __name__ == '__main__':
    target = 7
    array = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]

    res = Solution()
    print(res.Find1(target, array))
    print(res.Find2(target, array))
