nums = [4, 3, 2, 7, 8, 2, 3, 1]
# nums = [1, 1]

# nums = [1, 2, 3, 4, 7, 8]
# nums = [1, 2, 3, 4, 5, 6, 7, 8]


class Solution(object):
    def findDisappearedNumbers(self, nums):

        n = len(nums)
        ret = []
        nums = set(nums)

        for i in range(1, n + 1):
            if i not in nums:
                ret.append(i)

        return ret


Solution.findDisappearedNumbers(nums=nums)
