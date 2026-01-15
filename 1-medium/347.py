class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        arr = [[] for _ in range(n + 1)]

        hashmap = {}

        for num in nums:
            if not num in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for key, value in hashmap.items():
            arr[value].append(key)

        res = []
        counter = 0

        for i in range(n, 0, -1):
            if arr[i] != [] and counter < k:
                for x in arr[i]:
                    res.append(x)
                    counter += 1

        return res
