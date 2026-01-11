class Solution(object):
    def containsDuplicate(self, nums):

        x = set(nums)

        if len(nums) != len(x):
            return True

        return False
