class Solution(object):
    def twoSum(self, nums, target):

        _dict = {}

        for idx, value in enumerate(nums):
            if (target - value) not in _dict:
                _dict[value] = idx
            else:
                return [_dict[target - value], idx]
